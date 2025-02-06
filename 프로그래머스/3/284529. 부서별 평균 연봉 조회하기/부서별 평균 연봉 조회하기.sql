select d.DEPT_ID, d.DEPT_NAME_EN, ROUND(avg(e.SAL),0) AVG_SAL
from HR_DEPARTMENT d join HR_EMPLOYEES e on d.DEPT_ID = e.DEPT_ID
group by 1
order by 3 desc;