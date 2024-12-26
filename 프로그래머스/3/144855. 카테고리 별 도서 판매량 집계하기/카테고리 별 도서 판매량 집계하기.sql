-- 코드를 입력하세요
SELECT b.CATEGORY, sum(SALES) TOTAL_SALES
from BOOK b join BOOK_SALES bs on b.BOOK_ID = bs.BOOK_ID
where SALES_DATE like '%2022-01%'
group by 1
order by 1