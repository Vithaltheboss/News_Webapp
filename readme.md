News search apllication is a web application where user can search the news by providng the keyword. 

Functionalities of News search app
1. User can sign up or can directly login to news saerch app if already registered
2. After successful login user can able to search news by providing a keyword
3. Enter keyword in search box and hit the search button
4. Application will fetch all the news related to the keyword provided by user in search result
5. User can open the respective news by clicking on link 
6. Results search by user will be visible in news articles section of Admin 
7. Admin user can login to admin portal through admin page link
8. Admin can block or delete the user 
9. The user blocked by admin will not be able to login to application

prerequisites required to run the web app
1. User first need to register himself by clicking on sign up or can login directly by providing valid user name and password 

Installations & configuration 
1.clone the project & kept in a folder of local directory 
1.Activate the virtual envioronment by command promt
2.install the libraries from provided **requirements.txt** file (pip install -r requirements.txt)
3.set the cmd prompt directory to the project folder which consist manage.py cmd line utility
4.run command "python manage.py makemigrations"(to check model syntatically)
5.run command "python manage.py migrate"(to apply changes in model if any)
6.run command "python manage.py runserver"(to check model syntatically)
7.click on the generated url to browse the news search app. 
