-- Education --
-- Bikin schema baru lalu lanjut impor data csv kedalam scehma tersebut --

-- display data semua siswa --
SELECT * FROM education.student_sq;

-- display data siswa berdasarkan nilai mereka --
SELECT * FROM education.student_sq where Grade='AA';

-- display data siswa berdasarkan scholarship mereka --	
SELECT * FROM education.student_sq where Scholarship='100%';
show databases;
