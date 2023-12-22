# Django-Rest
/invoices/
/invoices/<int:pk>/



### Invoice rest API 
Some Sample Data 

Insert Data 
curl  -X POST  -H "Content-type: application/json" -d "{\"name\" : \"Jey\", \"description\" : \"Some text goes here\",\"quantity\" : 4,\"price\" : 4,\"unit_price\" : 4}" "https://inv.xapi.my.id/invoices"  

Update Data 
curl  -X POST  -H "Content-type: application/json" -d "{\"description\" : \"Some text goes here\",\"quantity\" : 4,\"price\" : 4,\"unit_price\" : 4}" "https://inv.xapi.my.id/invoices/1047"  

