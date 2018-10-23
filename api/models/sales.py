class Sales:
    sale_id = 0

    def __init__(self):

        self.sales = []
        self.sale_status = 'pending'
        '''
        The sales are a list of sales created in the store.
        '''

    def add_sale(self, **kwargs):

        '''
         sale_id will be created automatically.
         '''
        self.__class__.sale_id += 1
        self.product_name = kwargs.get("product_name")
        self.customer_name = kwargs.get("customer_name")
        self.product_quantity = kwargs.get("product_quantity")
        self.product_price = kwargs.get("product_price")
        self.sale_date_timestamp = kwargs.get("sale_date")
        self.sale_id = kwargs.get("sale_id")
        self.sales.append({
            'saleID': self.sale_id,
            'productName': self.product_name,
            'productQuantity': self.product_quantity,
            'productprice': self.product_price,
            'customerName': self.customer_name,
            'saleStatus': self.sale_status,
            'saleDate': self.sale_date_timestamp

        })

    def get_sales(self):
        if len(self.sales) > 0:
            return self.sales

    def get_sale_by_id(self, id):
        for sale in self.sales:
            if sale['id'] == id:
                self.sales.append(sale)
        if len(self.sales) > 0:
            return self.sales
