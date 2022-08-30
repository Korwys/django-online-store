# Shop Django+DRF 


## installation
1. install python3.10 
2. install PostgreSQL
2. install poetry <a href="https://python-poetry.org/docs/#installation" target="_blank">here</a> 
1. run command: poetry install
2. configure .env_template file in mainapp and rename it to .env
1. python manage.py migrate
1. python manage.py createsuperuser(insert username and password)
1. python manage.py runserver
---

# api paths
* [**api/v1/**](#apiv1)
	* [**api/v1/products/**](#apiv1products)
		* [**api/v1/products/?search={query}**](#apiv1productssearchquery)
	* [**api/v1/categories/**](#apiv1categories)
		* [**api/v1/categories/?search={query}**](#apiv1categoriessearchquery)
    * [**api/v1/gender/**](#apiv1genders)
	* [**api/v1/brands/**](#apiv1brands)
		* [**api/v1/brands/?search={query}**](#apiv1brandssearchquery)

	* [**api/v1/orders/**](#apiv1orders)
	* [**api/v1/orders/create/**](#apiv1create)
	* [**api/v1/orders/delete/<int:id>/**](#apiv1cartdeleteid)
  
	* [**api/v1/wishlists/**](#apiv1wishlists)
	* [**api/v1/wishlists/delete/<int:id>**](#apiv1wishlistsdeleteintid)
	* [**api/v1/wishlists/add/**](#apiv1wishlistadd)
  
	* [**api/v1/carts/**](#apiv1carts)
	* [**api/v1/carts/add/<int:id>**](#apiv1cartsaddintid)
	* [**api/v1/carts/update/<int:id>/<int:quality>**](#apiv1cartsupdateidquantityid)
	* [**api/v1/carts/delete/**](#apiv1cartdelete)


* [**api/v1/auth/**](#auth)
	* [**login/**](#authlogin)
	* [**logout/**](#authlogout)

___	
## api/v1/

### api/v1/products/
**Allowed Methods** : GET/POST/PUT/DELETE
<br>**Access Level** : IsStaffOrReadOnly
<br> Return array of objects of all products. Only staff can POST/PUT/DELETE.


### api/v1/products/?search={query}
**Allowed Methods** : GET/POST/PUT/DELETE
<br>**Access Level** : IsStaffOrReadOnly
<br> Search in products by product name and product price.


### api/v1/categories/
**Allowed Methods** : GET/POST/PUT/DELETE
<br>**Access Level** : IsStaffOrReadOnly
<br> Return array of objects of all categories. Only staff can POST/PUT/DELETE.


### api/v1/categories/?search={query}
**Allowed Methods** : GET/POST/PUT/DELETE
<br>**Access Level** : IsStaffOrReadOnly
<br> Search in categories by categories name.


### api/v1/genders/
**Allowed Methods** : GET/POST/PUT/DELETE
<br>**Access Level** : IsStaffOrReadOnly
<br> Return array of objects of all genders. Only staff can POST/PUT/DELETE.


### api/v1/brands/
**Allowed Methods** : GET/POST/PUT/DELETE
<br>**Access Level** : Authorized users
<br>return array of objects of all brands by user which is_authenticated.


### api/v1/brands?search={query}
**Allowed Methods** : GET/POST/PUT/DELETE
<br>**Access Level** : IsStaffOrReadOnly
<br> Search in brands by brands name.


### api/v1/orders/
**Allowed Methods** : GET/POST/PUT/DELETE
<br>**Access Level** : IsStaffOrReadOnly
<br> Return array of objects of all products. Only staff can POST/PUT/DELETE.


#### api/v1/orders/delete/<int:id>
**Allowed Methods** : DELETE
<br>**Access Level** : Authorized users
<br> Removes the order with the specified id


#### api/v1/orders/create/
**Allowed Methods** : POST
<br>**Access Level** : Authorized users
<br> Create order


### api/v1/wishlists/
**Allowed Methods** : GET
<br>**Access Level** : Authorized users
<br>return array of objects of all products which user added in wishlist.


### api/v1/wishlists/delete/<int:id>
**Allowed Methods** : DELETE
<br>**Access Level** : Authorized users
<br> Delete selected product from wishlist.


### api/v1/wishlists/add/<int:id>
**Allowed Methods** : POST
<br>**Access Level** : Authorized users
<br> Add selected product in user's wishlist.


### api/v1/carts/
**Allowed Methods** : GET
<br>**Access Level** : Authorized users
<br> Return array of objects of all products which user add to cart.


### api/v1/carts/add/<int:id>
**Allowed Methods** : POST
<br>**Access Level** : Authorized users
<br> Add selected product in user's cart.


### api/v1/carts/update/<int:id>/<int:quantity>/
**Allowed Methods** : PUT
<br>**Access Level** : Authorized users
<br> Сhanges the quantity of the selected product in cart.


### api/v1/carts/delete/<int:id>/
**Allowed Methods** : DELETE
<br>**Access Level** : Authorized users
<br> Delete selected product form user's cart.


## api/v1/auth/
### login/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'username', 'password'}
<br>*POST :* the data you post should include 'username' and 'password' fields if the user was authorized the access token and the refresh token will return as json.[more information about JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#usage)


### logout/
**allowed methods** : POST
<br>**Access Level** : Authorized users
<br>**fields :** 'required': {'refresh_token'}
<br>*POST :* should include the authorized user access token. post user refresh token with 'refresh_token' key to expire the access and refresh token of the given user.


