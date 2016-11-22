1. Install Oscar:

   ```bash
   pip install django-oscar==1.3
   ```
All other requirements come with oscar (pillow, django-1.9, haystack, etc). 

2. Create database:

   ```bash
   demo/manage.py migrate
   ```

3. Add superuser (log in by email, not login):
   
   ```bash
   demo/manage.py createsuperuser
   ```
   
4. Run server:
   
   ```bash
   demo/manage.py runserver
   ```
