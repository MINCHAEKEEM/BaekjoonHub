-- 코드를 입력하세요
SELECT WAREHOUSE_ID,
       WAREHOUSE_NAME,
       ADDRESS,
       if(FREEZER_YN is NULL, 'N', FREEZER_YN) FREEZER_YN
from FOOD_WAREHOUSE
where ADDRESS like '경기도%'
order by 1