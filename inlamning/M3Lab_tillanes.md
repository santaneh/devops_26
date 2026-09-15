1. Första rad avgör vilken python imagen    bygger på. 

COPY app och copy test körs varhe gång man ändrar på koden. Om RUN skulle vara efter app skulle det köras varje gång. 

EXPOSE 8000 gör inte porten nåbar. Utanför containern.

![Gissning 3 test](image-7.png)

![Test fungerar](image-8.png)

2. Det finns ingen RUN för att dockerfilen konfiguerear barA NGINX filen. Rad proxy_pass http://backend:8000/api/; talar med backenden. Backend namnet kommer från vår folder structure. 

![Steg 3](image-9.png)

![Webbläsare](image-10.png)

![Docker compose up](image-11.png)