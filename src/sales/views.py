from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SalesSearchForm
import pandas as pd
from .utils import get_salesman_from_id, get_customer_from_id

# Create your views here.

def home_view(request):
    form = SalesSearchForm(request.POST or None)

    sales_df = None
    positions_df = None
    merged_df = None

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
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
            # print('positions_df')
            # print(positions_df)

            sales_df = sales_df.to_html
            positions_df = positions_df.to_html
            merged_df = merged_df.to_html
            # print(sales_df)
            # print('#################')

            # # Dataframe without headers only numbers
            # df2 = pd.DataFrame(qs.values_list())
            # print(df2)

        else:
            print('No data')
    context = {
        'form': form,
        'sales_df': sales_df,
        'positions_df': positions_df,
        'merged_df': merged_df,
    }
    return render(request, 'sales/home.html', context)

class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = 'qs'

class SaleDetailView(DetailView):
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
 