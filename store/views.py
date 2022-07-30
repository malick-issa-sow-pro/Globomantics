from django.shortcuts import render, HttpResponse
from .models import Product, Category
from rest_framework import viewsets
from .serializers import ProductSerializers, CategorySerializers
import requests as requests_api
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, PageNotAnInteger

""" Multiple lines comment"""


# For Product API
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


@csrf_exempt
@require_http_methods(['GET', 'POST'])
# For render view for product
def all_products(request):
    if request.method == 'GET':
        # print the headers of the request
        print("\n----------------The-headers-of-the-GET-Request------------\n")
        print(request.headers)
        print("\n--------------end-The-headers-of-the-GET-Request-----\n")

        # print the body of the request
        print("\n----------------The-body-of-the-GET-Request------------\n")
        print(request.body)
        print("\n--------------end-The-body-of-the-GET-Request-----\n")

        # count_product = Product.objects.count()
        # products = Product.objects.all()

        # pull data from third party rest api
        response_api = requests_api.get('https://bit.ly/3PR0R3A')

        # print the response of the request
        print("\n----------------The-response-of-the-GET-Request-api-----------\n")
        print(f"The response of the GET Request api {response_api.status_code}")
        print("\n--------------end-The-response-of-the-GET-Request-api----\n")

        # print the Headers of the request api
        print("\n----------------The-Headers-of-the-GET-Request-api-----------\n")
        print(f"The headers of response of the GET method for api is : {response_api.headers} ")
        print("\n--------------end-The-Headers-of-the-GET-Request-api----\n")

        # print the cookies of the request api
        print("\n----------------The-cookies-of-the-GET-Request-api-----------\n")
        print(f"The cookies of response of the GET method for api is : {response_api.cookies} ")
        print("\n--------------end-The-cookies-of-the-GET-Request-api----\n")

        # print the history of the request api
        print("\n----------------The-history-of-the-GET-Request-api-----------\n")
        print(f"The history of response of the GET method for api is : {response_api.history} ")
        print("\n--------------end-The-history-of-the-GET-Request-api----\n")

        # convert response data to json
        products = response_api.json()
        # print the product give by the response of the request api
        print("\n----------------The-product-give-by-the-response-of-the-GET-Request-api-----------\n")
        print(f"The product give by the response of the GET method for api is : {products} ")
        print("\n--------------end-The-product-give-by-the-response-of-the-GET-Request-api----\n")

        number_product = len(products)

        # pagination
        paginator = Paginator(products, 2)
        numero_page = request.GET.get('page', 1)
        try:
            products = paginator.page(numero_page)
        except PageNotAnInteger:
            products = paginator.page(1)

        return render(
            request,
            'store/product/all_product.html',
            {
                'number_product': number_product,
                'products': products,
            }

        )
    elif request.method == 'POST':
        return HttpResponseNotFound("Post Method not Allowed here")


def on_product(request, id):
    # product_details = get_object_or_404(Product, pk=id)
    # get products from api
    response = requests_api.get('https://bit.ly/3PR0R3A')
    products = response.json()
    for product in products:
        if product['id'] == id:
            return render(
                request,
                'store/product/one_product.html',
                {
                    'product': product
                }
            )


# For Category API
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


# For View
def all_category(request):
    # count_category = Category.objects.count()
    # category = Category.objects.all()  # [0:3]
    # pull data from third party api
    get_all_category = requests_api.get('https://bit.ly/3IWPXa5')
    category = get_all_category.json()
    count_category = len(category)
    paginator = Paginator(category, 2)
    numero_page = request.GET.get('page',1)
    try:
        category = paginator.page(numero_page)
    except PageNotAnInteger:
        category = paginator.page(1)
    return render(
        request,
        'store/category/all_category.html',
        {
            'number_category': count_category,
            'category': category,
        }
    )


def get_one_category(request, id):
    response = requests_api.get('https://bit.ly/3IWPXa5')
    category = response.json()
    for one_category in category:
        if one_category['id'] == id:
            return render(
                request,
                'store/category/one_category.html',
                {
                    'one_category': one_category,
                }
            )
