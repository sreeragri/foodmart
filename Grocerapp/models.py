from django.db import models

# Create your models here.
class tbl_signup(models.Model):
    Username=models.CharField(max_length=50,null=True)
    Mobile=models.IntegerField(null=True)
    Password=models.CharField(max_length=50,null=True)


class tbl_category(models.Model):
    categoryname=models.CharField(max_length=35,null=True)
    categoryimage=models.ImageField(upload_to="media",null=True)
    categorystatus=models.CharField(max_length=40,null=True)

class tbl_SubCategory(models.Model):
    category = models.ForeignKey(tbl_category, on_delete=models.CASCADE)
    SubCategoryname=models.CharField(max_length=30,null=True)
    SubCategoryimage=models.ImageField(upload_to="media",null=True)
    SubCategorystatus=models.CharField(max_length=30,null=True)

class tbl_Products(models.Model):
    Productname=models.CharField(max_length=45,null=True)
    Productimage=models.ImageField(upload_to="media",null=True)
    Productprice=models.CharField(max_length=40,null=True)
    Productofferprice=models.IntegerField(null=True)
    Productweight=models.CharField(max_length=40,null=True)
    Productdescription=models.CharField(max_length=150,null=True)
    ProductNumofpieces=models.CharField(max_length=20,null=True)
    ProductStockin=models.CharField(max_length=40,null=True)
    ProductStockout=models.CharField(max_length=40,null=True)
    category=models.ForeignKey(tbl_category, on_delete=models.CASCADE,null=True)
    SubCategory=models.ForeignKey(tbl_SubCategory, on_delete=models.CASCADE,null=True)


class tbl_cart(models.Model):
    Product=models.ForeignKey(tbl_Products,on_delete=models.CASCADE,null=True)
    User=models.ForeignKey(tbl_signup,on_delete=models.CASCADE,null=True)
    Quantity=models.IntegerField(null=True)
    session_key=models.CharField(max_length=40,null=True)
    def total_price(self):
        return self.Quantity * self.Product.Productofferprice

class tbl_wishlist(models.Model):
    Product = models.ForeignKey(tbl_Products, on_delete=models.CASCADE, null=True)
    User = models.ForeignKey(tbl_signup, on_delete=models.CASCADE, null=True)
    session_key = models.CharField(max_length=40, null=True)

class tbl_order(models.Model):
    Fullname=models.CharField(max_length=40,null=True)
    Address=models.CharField(max_length=300,null=True)
    Phonenumber=models.IntegerField(null=True)
    Paymentmethod=models.CharField(max_length=50,null=True)
    Total_price=models.IntegerField(null=True)
    User=models.ForeignKey(tbl_signup,on_delete=models.CASCADE,null=True)
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    Status=models.CharField(max_length=40,choices=STATUS_CHOICES,default='Pending')



class tbl_order_item(models.Model):
    Product = models.ForeignKey(tbl_Products, on_delete=models.CASCADE, null=True)
    User = models.ForeignKey(tbl_signup, on_delete=models.CASCADE, null=True)
    Quantity = models.IntegerField(null=True)
    session_key = models.CharField(max_length=40, null=True)

    order = models.ForeignKey(tbl_order, on_delete=models.CASCADE, null=True)

    def total_price(self):
        return self.Quantity * self.Product.Productofferprice

class tbl_Delivery_partners(models.Model):
    Name=models.CharField(max_length=100,null=True)
    Contact=models.IntegerField(null=True)
    Age=models.IntegerField(null=True)
    Address=models.CharField(max_length=300,null=True)
    Vehicledetails=models.CharField(max_length=50,null=True)
    Email=models.CharField(max_length=50,null=True)
    Password=models.CharField(max_length=50,null=True)

class Tbl_order_assign(models.Model):
    createdtime=models.DateTimeField(auto_now_add=True,null=True)
    partner_id=models.ForeignKey(tbl_Delivery_partners,on_delete=models.CASCADE,null=True,related_name='Delivery')
    order_id=models.ForeignKey(tbl_order,on_delete=models.CASCADE,null=True,related_name='Delivery_order')

class Tbl_contact_page(models.Model):
    contactname=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    subject=models.CharField(max_length=500,null=True)
    message=models.CharField(max_length=500,null=True)















