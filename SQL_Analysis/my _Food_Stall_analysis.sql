create database food_businesss;
use food_businesss;
CREATE TABLE food_sales (
    Date VARCHAR(20),
    Day VARCHAR(20),
    Weekend VARCHAR(10),
    Public_Holiday VARCHAR(10),
    Weather VARCHAR(20),
    Time_Slot VARCHAR(20),
    Product VARCHAR(50),
    Total_Quantity_Prepared INT,
    Quantity_Sold INT,
    Selling_Price INT,
    Revenue INT,
    Estimated_Cost FLOAT,
    Profit FLOAT,
    Net_Profit_Loss FLOAT,
    Payment_Mode VARCHAR(20),
    Platform VARCHAR(20)
);
-- 1.Total Revenue
SELECT SUM(Revenue) AS Total_Revenue
FROM food_sales;

-- 2.Net Profit_Loss.
select sum(Net_Profit_Loss) as Net_Profit_Loss
from food_sales;

-- 3.Product Wise Revenue.
select Product,
sum(Revenue) as Revenue
from food_sales
group by Product
order by Revenue Desc;

-- 4.Product Wise Net Profit OR Loss.
select Product ,
sum(Net_Profit_Loss) as Net_Profit_Loss
from food_sales
group by Product
order by Net_Profit_Loss;

-- 5.Weekend Analysis.
select Weekend ,Sum(Revenue) as Revenue
from food_sales
group by Weekend;

-- 6.Weather Analysis.
Select Weather, sum(Net_Profit_Loss) as NETloss,
sum(Revenue) as revenue
From food_sales
group by Weather;

-- 7.PlatForm Analysis.
Select Platform, sum(Net_Profit_Loss) AS Net_Profit_Loss
from food_sales
group by Platform;

-- 8.Payment Mode analysis.
Select Payment_Mode,
    sum(Revenue) as Revenue
    from food_sales
    group by payment_mode;
    
-- 9.Monthly Revenue Trend.
SELECT 
    MONTHNAME(STR_TO_DATE(`Date`, '%d-%m-%Y')) AS Month,
    SUM(Revenue) AS Revenue
FROM food_sales
GROUP BY Month
ORDER BY FIELD(
    Month,
    'August',
    'September',
    'October',
    'November',
    'December',
    'January',
    'February',
    'March',
    'April',
    'May'
);

-- 10.Product Wastage Analysis.
SELECT 
    Product,
    SUM(Total_Quantity_Prepared - Quantity_Sold) AS Total_Wastage
FROM food_sales
group by Product
ORDER BY Total_Wastage DESC;   
 
-- 11. Weekday vs Weekend Profitability Analysis .
   select weekend , sum(Revenue) as total_revenue,
   sum(Net_Profit_Loss) as Net_p_l
   from food_sales
   group by weekend;

-- 12.Top 5 Loss Making Products.
select Product,sum(Net_Profit_Loss) as total_loss
from food_sales
group by  Product 
Order by total_loss asc 
limit 5;

-- SQL analysis helped convert raw sales data into meaningful business insights by identifying
 -- the major reasons behind the business loss, such as low weekday demand, Food wastage,
  -- limited customer demand and high operational costs,platform commission impact.