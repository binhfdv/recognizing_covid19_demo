# Hệ thống demo đề tài Nhận diện COVID-19 qua âm thanh tiếng ho

## Hướng dẫn
1. Clone repo này theo cú pháp:
```git clone git@github.com:githubbinh/recognizing_covid19_demo.git```
2. Di chuyển vào thư mục repo: ```cd recognizing_covid19_demo```
3. Cài đặt các thư viện:
```pip install -r requirements.txt ```
4. Tải các mô hình Cough Detection và COVID-19 Cough Recognition:
```dvc pull```
5. Khởi động back end
```cd src/backend/```
```python manage.py runserver```
6. Khởi động front end
```cd src/frontend/```
```npm run serve```
