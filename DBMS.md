Structured Query language :-
Strucrured means there is human understandable language 
SQL is used to communicte with the database


SQL vs CSV
----------------------------------------------------------------------------------------------
1.Data intigrity .
2.Fast and effective to store large volume of data .
3.supports multiple users simultaneously.
4.Built in backups and recovery options .
5.SQl query engine is built in C++ so its is very fast to search 
6.Role baes access and permission .
----------------------------------------------------------------------------------------------

-- QuickCart Database Select Karna
USE quickcart;

-- Cancelled orders ko display karo
SELECT *
FROM orders
WHERE Status = "Cancelled";

-- Top 5 orders jinki quantity sabse zyada hai
SELECT *
FROM orders
ORDER BY Quantity DESC
LIMIT 5;

-- CustomerID = 8 ke orders ko quantity ke descending order me dikhao
SELECT *
FROM orders
WHERE CustomerID = 8
ORDER BY Quantity DESC;

-- Sabse sasta product (minimum price wala)
SELECT ProductName, Price
FROM products
WHERE Price = (
    SELECT MIN(Price)
    FROM products
);

-- 1 June 2026 ko place hue orders
SELECT *
FROM orders
WHERE OrderDate = "2026-06-01";

-- Latest 4 orders (OrderDate ke basis par)
SELECT *
FROM orders
ORDER BY OrderDate DESC
LIMIT 4;

-- CustomerID = 1 ke top 2 sabse mehange orders
SELECT *
FROM orders
WHERE CustomerID = 1
ORDER BY Amount DESC
LIMIT 2;

-- Grocery category ke products jinka stock 30 hai
SELECT ProductName, StockLeft
FROM products
WHERE Category = "Grocery"
AND StockLeft = 30;

-- CustomerID = 1 ke scrap orders
SELECT OrderID, Amount, Status
FROM orders_scrap
WHERE CustomerID = 1;

-- Srinagar ya Katra ke customers
SELECT CustomerID, FullName
FROM customers
WHERE City = "Srinagar"
OR City = "Katra";

-- Grocery ya Stationery category ke products
SELECT ProductID, ProductName
FROM products
WHERE Category = "Grocery"
OR Category = "Stationery";

-- Grocery aur Stationery ek saath (Impossible condition)
-- Is query ka result Empty aayega
SELECT ProductID, ProductName
FROM products
WHERE Category = "Grocery"
AND Category = "Stationery";

-- Jinka naam S se start hota hai
SELECT *
FROM customers
WHERE FullName LIKE "S%";

-- Jinke naam me "Kh" kahin bhi ho
SELECT *
FROM customers
WHERE FullName LIKE "%Kh%";

-- Jinka naam a se end hota hai
SELECT *
FROM customers
WHERE FullName LIKE "%a";

-- Product name me "Notes" ho
SELECT *
FROM products
WHERE ProductName LIKE "%Notes%";

-- Product name me "Oil" ho
SELECT *
FROM products
WHERE ProductName LIKE "%Oil%";

-- Delhi ke customers jinke phone me 98 ho
SELECT *
FROM customers
WHERE City = "Delhi"
AND Phone LIKE "%98%";

-- Delhi me kitne customers hain
SELECT COUNT(FullName)
FROM customers
WHERE City = "Delhi";

-- Delhi me total rows count
SELECT COUNT(*)
FROM customers
WHERE City = "Delhi";

-- Har city me kitne customers hain
SELECT COUNT(FullName), City
FROM customers
GROUP BY City;

-- Har category me kitne products hain
SELECT COUNT(Category), Category
FROM products
GROUP BY Category;

-- Sab products ki total price
SELECT SUM(Price)
FROM products;

-- Minimum price
SELECT MIN(Price)
FROM products;

-- Average price
SELECT AVG(Price)
FROM products;

-- Maximum price
SELECT MAX(Price)
FROM products;

-- Total customers
SELECT COUNT(*)
FROM customers;

-- Total products
SELECT COUNT(*)
FROM products;

-- Products ka summary (Min, Max, Avg Price aur Total Stock)
SELECT
    MIN(Price),
    MAX(Price),
    AVG(Price),
    SUM(StockLeft)
FROM products;

-- Cancelled orders ki total amount aur total cancelled orders
SELECT
    SUM(Amount),
    COUNT(*)
FROM orders
WHERE Status = "Cancelled";

-- Har customer ne kitne orders place kiye
SELECT
    CustomerID,
    COUNT(OrderID)
FROM orders
GROUP BY CustomerID;

-- Har product ki total sold quantity
SELECT
    ProductID,
    SUM(Quantity) AS Quantity
FROM orders
GROUP BY ProductID
ORDER BY Quantity DESC;

-- Har date ki total sales, top 4 dates
SELECT
    SUM(Amount) AS TotalSales,
    OrderDate
FROM orders
GROUP BY OrderDate
ORDER BY SUM(Amount) DESC
LIMIT 4;


SELECT *
    -> FROM customers
    -> JOIN orders
    -> ON customers.CustomerID = orders.CustomerID;

CREATE VIEW customer_orders AS
    -> SELECT
    ->     c.CustomerID,
    ->     c.Fullname,
    ->     c.City,
    ->     o.ProductID,
    ->     o.OrderDate,
    ->     o.Status
    -> FROM customers c
    -> JOIN orders o
    -> ON c.CustomerID = o.CustomerID;

Here c,o are alias name of customer table and order table

SELECT * FROM customers LEFT JOIN orders ON customers.CustomerID = orders.CustomerID;

SELECT 
    p.ProductID, 
    p.ProductName, 
    p.Price,
    SUM(o.Quantity) AS TotalQuantitySold
FROM products p
LEFT JOIN orders o ON p.ProductID = o.ProductID
GROUP BY p.ProductID, p.ProductName, p.Price
ORDER BY TotalQuantitySold DESC
LIMIT 5;

-- Select Product Name, Category, and Order Amount
SELECT 
    p.ProductName,   -- Product ka naam
    p.Category,      -- Product ki category
    o.Amount         -- Order ki total amount
FROM orders o        -- Orders table ko 'o' alias diya
JOIN products p      -- Products table ko 'p' alias diya
ON p.ProductID = o.ProductID;   -- Dono tables ko ProductID ke basis par join kiya


-- Customer Details
SELECT *
FROM customers;

-- Product Details
SELECT *
FROM products;

-- Orders Details
SELECT *
FROM orders;

-- Order Details + Product Details (JOIN)
SELECT *
FROM orders o
JOIN products p ON o.ProductID = p.ProductID;

-- Customer + Order Details (JOIN)
SELECT *
FROM customers c
JOIN orders o ON c.CustomerID = o.CustomerID;

-- Full Details: Customer + Order + Product (JOIN)
SELECT *
FROM customers c
JOIN orders o ON c.CustomerID = o.CustomerID
JOIN products p ON o.ProductID = p.ProductID;