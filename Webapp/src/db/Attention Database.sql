-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 06, 2020 at 08:25 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ATTENTION DATABASE`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_Attention`
--

CREATE TABLE `tbl_Attention` (
  `id` int(10) NOT NULL,
  `Class_id` int(11) NOT NULL,
  `Date` date NOT NULL,
  `Start_Time` time(5) NOT NULL,
  `End_Time` time(5) NOT NULL,
  `Average_Attention` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_Attention`
--

INSERT INTO `tbl_Attention` (`id`, `Class_id`, `Date`, `Start_Time`, `End_Time`, `Average_Attention`) VALUES
(1, 1, '2020-02-12', '10:00:00.00000', '11:00:00.00000', 0.7),
(3, 2, '2020-02-13', '11:00:00.00000', '12:00:00.00000', 0.6),
(4, 3, '2020-02-13', '00:00:12.00000', '00:00:01.00000', 0.6);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_class`
--

CREATE TABLE `tbl_class` (
  `Class_id` int(40) NOT NULL,
  `Weekday` varchar(15) NOT NULL,
  `Subject_id` int(15) NOT NULL,
  `Teacher_id` int(10) NOT NULL,
  `Location` varchar(15) NOT NULL,
  `Start_Time` time(5) NOT NULL,
  `End_Time` time(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_department`
--

CREATE TABLE `tbl_department` (
  `Dept_code` varchar(10) NOT NULL,
  `Subject_id` int(10) NOT NULL,
  `Teacher_id` int(10) NOT NULL,
  `Dept_Name` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_time`
--

CREATE TABLE `tbl_time` (
  `Average_Attention` float NOT NULL,
  `Time_Duration` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_Attention`
--
ALTER TABLE `tbl_Attention`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_Attention`
--
ALTER TABLE `tbl_Attention`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
