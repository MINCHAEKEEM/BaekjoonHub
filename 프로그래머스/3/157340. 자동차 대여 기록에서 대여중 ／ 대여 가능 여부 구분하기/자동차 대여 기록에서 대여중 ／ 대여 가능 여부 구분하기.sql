-- 코드를 입력하세요
SELECT CAR_ID,
       case when max('2022-10-16' between START_DATE and END_DATE) = 1 then '대여중'
            else '대여 가능' end AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
group by 1
order by 1 desc

