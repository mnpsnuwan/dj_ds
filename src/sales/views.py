from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SalesSearchForm
from reports.forms import ReportForm
import pandas as pd
from .utils import get_salesman_from_id, get_customer_from_id, get_chart

# protect views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required
def home_view(request):
    sales_df = None
    positions_df = None
    merged_df = None
    df = None
    chart = None
    no_data = None

    search_form = SalesSearchForm(request.POST or None)
    report_form = ReportForm()

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        results_by = request.POST.get('results_by')
        # print(date_from, date_to, chart_type)

        sale_qs = Sale.objects.filter(created__date__gte=date_from, created__date__lte=date_to)
        if len(sale_qs) > 0:
            # obj = Sale.objects.get(id=1)
            # print(qs)
            # print(obj)
            # print(qs.values())
            # print(qs.values_list())

            # print('===================================')
            # Dataframe with headers
            sales_df = pd.DataFrame(sale_qs.values())
            sales_df['customer_id'] = sales_df['customer_id'].apply(get_customer_from_id)  # Return the customer for customer id
            sales_df['salesman_id'] = sales_df['salesman_id'].apply(get_salesman_from_id)  # Return the salesman for salesman id
            sales_df['created'] = sales_df['created'].apply(lambda x: x.strftime('%Y-%m-%d'))  # Return the salesman for salesman id

            # sales_df = sales_df.rename({'customer_id': 'customer', 'salesman_id': 'salesman'}, axis=1)
            sales_df.rename({'customer_id': 'customer', 'salesman_id': 'salesman', 'id': 'sales_id'}, axis=1, inplace=True)  # Same as above using inplace=True
            # sales_df['sales_id'] = sales_df['id']

            positions_data = []

            for sale in sale_qs:
                for pos in sale.get_positions():
                    obj = {
                        'position_id': pos.id,
                        'product': pos.product.name,
                        'quantity': pos.quantity,
                        'price' : pos.price,
                        'sales_id': pos.get_sales_id(),
                    }
                    positions_data.append(obj)

            positions_df = pd.DataFrame(positions_data)
            merged_df = pd.merge(sales_df, positions_df, on='sales_id')
            df = merged_df.groupby('transaction_id', as_index=False)['price'].agg('sum')
            # print('positions_df')
            # print(positions_df)

            chart = get_chart(chart_type, sales_df, results_by)

            sales_df = sales_df.to_html
            positions_df = positions_df.to_html
            merged_df = merged_df.to_html
            df = df.to_html
            # print(sales_df)
            # print('#################')

            # # Dataframe without headers only numbers
            # df2 = pd.DataFrame(qs.values_list())
            # print(df2)

        else:
            no_data = 'No data is available in this date range'

    context = {
        'search_form': search_form,
        'report_form': report_form,
        'sales_df': sales_df,
        'positions_df': positions_df,
        'merged_df': merged_df,
        'df': df,
        'chart': chart,
        'no_data': no_data,
    }
    return render(request, 'sales/home.html', context)

class SaleListView(LoginRequiredMixin, ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = 'qs'

class SaleDetailView(LoginRequiredMixin, DetailView):
    model = Sale
    template_name = 'sales/detail.html'
    context_object_name = 'obj'

# SaleListView using function
# def sale_list_view(request):
#     qs = Sale.objects.all()
#     return render(request, 'sales/main.html', {'qs':qs})

# # SaleDetailView using function
# def sale_detail_view(request, **kwargs):
#     pk = kwargs.get('pk')
#     obj = Sale.objects.get(pk=pk)
#     return render(request, 'sales/detail.html', {'obj':obj})
 