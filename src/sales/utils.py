import uuid, base64
from customers.models import Customer
from .models import Profile
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns

def generate_code():
    code = str(uuid.uuid4()).replace('-','').upper()[:12]
    return code

def get_salesman_from_id(val):
    salesman = Profile.objects.get(id=val)
    return salesman.user.username

def get_customer_from_id(val):
    customer = Customer.objects.get(id=val)
    return customer

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10, 4))
    if chart_type == '#1':
        print('bar chart')
        # plt.bar(data['transaction_id'], data['price'])
        sns.barplot(x='transaction_id', y='price', data=data)
    elif chart_type == '#2':
        print('pie chart')
        labels = kwargs.get('labels')
        plt.pie(data=data, x='price', labels=labels)
    elif chart_type == '#3':
        print('line chart')
        plt.plot(data['transaction_id'], data['price'], color='green', marker='o', linestyle='dashed')
    else:
        print('ups... failed to identify the chart type')
    
    plt.tight_layout()
    chart = get_graph()
    return chart