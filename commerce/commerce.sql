-- bikin tabel
USE commerce;
CREATE TABLE Shipments (
    ID INT PRIMARY KEY,
    Warehouse_block CHAR(1),
    Mode_of_Shipment VARCHAR(10),
    Customer_care_calls INT,
    Customer_rating INT,
    Cost_of_the_Product INT,
    Prior_purchases INT,
    Product_importance VARCHAR(10),
    Gender CHAR(1),
    Discount_offered INT,
    Weight_in_gms INT,
    Reached_on_Time_Y_N INT
);

-- isi tabel
INSERT INTO Shipments (ID, Warehouse_block, Mode_of_Shipment, Customer_care_calls, Customer_rating, Cost_of_the_Product, Prior_purchases, Product_importance, Gender, Discount_offered, Weight_in_gms, Reached_on_Time_Y_N) VALUES
(1, 'D', 'Flight', 4, 2, 177, 3, 'low', 'F', 44, 1233, 1),
(2, 'F', 'Flight', 4, 5, 216, 2, 'low', 'M', 59, 3088, 1),
(3, 'A', 'Flight', 2, 2, 183, 4, 'low', 'M', 48, 3374, 1),	
(4, 'B', 'Flight', 3, 3, 176, 4, 'medium', 'M', 10, 1177, 1),
(5, 'C', 'Flight', 2, 2, 184, 3, 'medium', 'F', 46, 2484, 1),
(6, 'F', 'Flight', 3, 1, 162, 3, 'medium', 'F', 12, 1417, 1),
(7, 'D', 'Flight', 3, 4, 250, 3, 'low', 'F', 3, 2371, 1),
(8, 'F', 'Flight', 4, 1, 233, 2, 'low', 'F', 48, 2804, 1),
(9, 'A', 'Flight', 3, 4, 150, 3, 'low', 'F', 11, 1861, 1),
(10, 'B', 'Flight', 3, 2, 164, 3, 'medium', 'F', 29, 1187, 1),
(11, 'C', 'Flight', 3, 4, 189, 2, 'medium', 'M', 12, 2888, 1),
(12, 'F', 'Flight', 4, 5, 232, 3, 'medium', 'F', 32, 3253, 1),
(13, 'D', 'Flight', 3, 5, 198, 3, 'medium', 'F', 1, 3667, 1),
(14, 'F', 'Flight', 4, 4, 275, 3, 'high', 'M', 29, 2602, 1),
(15, 'A', 'Flight', 4, 3, 152, 3, 'low', 'M', 43, 1009, 1),
(16, 'B', 'Flight', 4, 3, 227, 3, 'low', 'F', 45, 2707, 1),
(17, 'C', 'Flight', 3, 4, 143, 2, 'medium', 'F', 6, 1194, 1),
(18, 'F', 'Ship', 5, 5, 227, 3, 'medium', 'M', 36, 3952, 1),
(19, 'D', 'Ship', 5, 5, 239, 3, 'high', 'M', 18, 2495, 1),
(20, 'F', 'Ship', 4, 5, 145, 3, 'medium', 'M', 45, 1059, 1),
(21, 'A', 'Ship', 3, 3, 161, 2, 'medium', 'F', 38, 1521, 1),
(22, 'B', 'Ship', 3, 1, 232, 4, 'medium', 'F', 51, 2899, 1),
(23, 'C', 'Ship', 2, 5, 156, 2, 'low', 'M', 2, 1750, 1),
(24, 'F', 'Ship', 4, 3, 211, 3, 'high', 'M', 12, 3922, 1),
(25, 'D', 'Ship', 4, 5, 251, 2, 'medium', 'F', 28, 3561, 1),
(26, 'F', 'Ship', 3, 1, 225, 4, 'low', 'M', 29, 3496, 1),
(27, 'A', 'Ship', 4, 1, 172, 3, 'high', 'F', 24, 1066, 1),
(28, 'B', 'Ship', 5, 1, 162, 3, 'medium', 'M', 31, 1435, 1),
(29, 'C', 'Ship', 2, 3, 234, 4, 'low', 'M', 44, 3134, 1),
(30, 'F', 'Ship', 5, 4, 183, 2, 'low', 'F', 36, 3819, 1);

-- display data
SELECT * FROM commerce.shipments;

-- jumlah produk yang on time
SELECT COUNT(*) AS tepat
FROM Shipments
WHERE Reached_on_Time_Y_N = 0;

-- jumlah produk yang terlambat
SELECT COUNT(*) AS terlambat
FROM Shipments
WHERE Reached_on_Time_Y_N = 1;

-- display data shipment yang terlambat
SELECT *
FROM Shipments
WHERE Reached_on_Time_Y_N = 1;

-- display distribusti shipping method yang terlambat
SELECT Mode_of_Shipment, COUNT(*) AS On_Time_Count
FROM Shipments
WHERE Reached_on_Time_Y_N = 1
GROUP BY Mode_of_Shipment
ORDER BY On_Time_Count DESC;

-- display distribus warehouse yang terlambat
SELECT Warehouse_block, COUNT(*) AS On_Time_Count
FROM Shipments
WHERE Reached_on_Time_Y_N = 1
GROUP BY Warehouse_block
ORDER BY On_Time_Count DESC;

-- display distribusi kepentingan yang terlambat
SELECT Product_importance, COUNT(*) AS On_Time_Count
FROM Shipments
WHERE Reached_on_Time_Y_N = 1
GROUP BY Product_importance
ORDER BY On_Time_Count DESC;

-- display kombinasi shipment, kepentingan, dan warehouse dengan jumlah keterlambatan tertinggi
SELECT Mode_of_Shipment, Product_importance, Warehouse_block, COUNT(*) AS Late_Count
FROM Shipments
WHERE Reached_on_Time_Y_N = 1
GROUP BY Mode_of_Shipment, Product_importance, Warehouse_block
ORDER BY Late_Count DESC;

select @ax := avg(Customer_rating) as 'Rata-rata customer_rating', 
       @ay := avg(Customer_care_calls) as 'Rata-rata customer_calls', 
       @div := (stddev_samp(Customer_rating) * stddev_samp(Customer_care_calls)) as 'selisih std'
from shipments;

select sum( ( Customer_rating - @ax ) * (Customer_care_calls - @ay) ) / ((count(Customer_rating) -1) * @div) as 'korelasi' from shipments;

select @ac := avg(Cost_of_the_Product) as 'Rata-rata harga barang' from shipments;
select ID, Mode_of_Shipment from shipments where Cost_of_the_Product < @ac;
select ID, Mode_of_Shipment from shipments where Cost_of_the_Product >= @ac;