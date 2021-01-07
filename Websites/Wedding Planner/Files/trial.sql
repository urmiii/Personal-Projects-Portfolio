-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 26, 2019 at 08:43 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `trial`
--

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `bname` varchar(20) NOT NULL,
  `gname` varchar(20) NOT NULL,
  `num` int(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pwd` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`bname`, `gname`, `num`, `email`, `uname`, `pwd`) VALUES
('alexa', 'bratt', 123456789, 'brat@gmail.com', 'amanda', '202cb962ac59075b964b'),
('priyamka', 'rushi', 2147483647, 'sushi@gmail.com', 'shutthe', '979d472a84804b9f647b'),
('priyamka', 'rushi', 2147483647, 'sushi@gmail.com', 'shutthe', '979d472a84804b9f647b'),
('priyamka', 'rushi', 2147483647, 'sushi@gmail.com', 'shutthe', '979d472a84804b9f647b'),
('jhanvi', 'nadeem', 123456789, 'nofg@gmail.com', 'buddy', 'e338bc584bd1c7f87b8a');

-- --------------------------------------------------------

--
-- Table structure for table `todo`
--

CREATE TABLE `todo` (
  `task` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `todo`
--

INSERT INTO `todo` (`task`) VALUES
('meghan markle'),
('harry styles'),
('urmi shah'),
('meghan markle'),
('meghan markle'),
('meghan markle'),
('meghan markle'),
('meghan markle');

-- --------------------------------------------------------

--
-- Table structure for table `trialtable`
--

CREATE TABLE `trialtable` (
  `uname` varchar(20) NOT NULL,
  `pwd` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `userpass`
--

CREATE TABLE `userpass` (
  `user` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userpass`
--

INSERT INTO `userpass` (`user`, `pass`) VALUES
('urmi', '202cb962ac59075b964b'),
('new', '22af645d1859cb5ca6da'),
('new', '22af645d1859cb5ca6da'),
('abc', '900150983cd24fb0d696'),
('abc', '900150983cd24fb0d696'),
('abc', '900150983cd24fb0d696'),
('urmi', '202cb962ac59075b964b'),
('urmi', '900150983cd24fb0d696');

-- --------------------------------------------------------

--
-- Table structure for table `validation`
--

CREATE TABLE `validation` (
  `namee` varchar(20) NOT NULL,
  `pwd` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `validation`
--

INSERT INTO `validation` (`namee`, `pwd`) VALUES
('', 'd41d8cd98f00b204e980'),
('', 'd41d8cd98f00b204e980'),
('', 'd41d8cd98f00b204e980'),
('', 'd41d8cd98f00b204e980'),
('', 'd41d8cd98f00b204e980');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
