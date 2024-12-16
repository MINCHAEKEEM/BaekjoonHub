-- 코드를 입력하세요
select count(age2) USERS
from
(
SELECT *, if(AGE is NULL, 'NULL', AGE) age2
from USER_INFO
where AGE is NULL
) a