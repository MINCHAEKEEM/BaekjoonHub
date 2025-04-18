-- 코드를 입력하세요
WITH JULY_TOTALS AS (
    SELECT 
        FLAVOR,
        SUM(TOTAL_ORDER) AS JULY_ORDER
    FROM 
        JULY
    GROUP BY 
        FLAVOR
),
FIRST_HALF_TOTALS AS (
    SELECT 
        FLAVOR,
        SUM(TOTAL_ORDER) AS FIRST_HALF_ORDER
    FROM 
        FIRST_HALF
    GROUP BY 
        FLAVOR
)
SELECT 
    J.FLAVOR
FROM 
    JULY_TOTALS J
LEFT JOIN 
    FIRST_HALF_TOTALS F
ON 
    J.FLAVOR = F.FLAVOR
ORDER BY 
    COALESCE(J.JULY_ORDER, 0) + COALESCE(F.FIRST_HALF_ORDER, 0) DESC
LIMIT 3;