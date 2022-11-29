# PCOS Project

Our project studies the relationship between gut bacteria and the presence of PCOS. Our project consists of two parts:
1. A Python notebook in which we investigated the relationship between gut bacteria and the diagnosis of PCOS. The code of this part is in the folder "PCOS-Jupyter-main". 
2. A website where a user can check her chances of PCOS based on two fields' input. The code of this part is in the folder "PCOS-Website-main".

How to use the files:
Unfortunately, the project's notebook, which investigates the relationship between gut bacteria and PCOS diagnosis, is based on a confidential dataset of DayTwo company.
Therefore, it is possible to browse the notebook code and its outputs using Jupyter but it is impossible to run it with the original data we used.
On the other hand, the website can be run locally on the computer by following the steps below:
0. Extract the code.zip folder
1. Navigate to '/code/PCOS-Website-main' with your CMD
If you have pip installed on your computer, skip 1.a
1.a. If you don't have pip installed on your CMD, run: 
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python3 get-pip.py
2. Using pip, run: $ pip install -r requirements.txt
Steps 3-5 will generate you a secret key which will be used to run the website:
3. Navigate to any other folder on your computer 
4. Run: $ django-admin startproject <name of the project> 
5. Now go to '<name of the project>/<name of the project>/setting.py' and copy the SECRET_KEY.
6. Open 'code/PCOS-Website-main/PCOS_website/settings.py' and paste the copied SECRET_KEY instead of the '****'.
7. Navigate to 'code/PCOS-Website-main' on your CMD
8. Run: $ python3 manage.py makemigrations
9. Run: $ python3 manage.py migrate
10. Create a user by running: $ python3 manage.py createsuperuser
11. Run: $ python3 manage.py runserver 
12. Go to your browser and paste: http://localhost:8000/ to 
your address bar
13. To stop the website's running, go to the CMD and press CTRL+C.

If you have any troubles running the website please contact us at the Email addresses: tamarsh224@gmail.com
