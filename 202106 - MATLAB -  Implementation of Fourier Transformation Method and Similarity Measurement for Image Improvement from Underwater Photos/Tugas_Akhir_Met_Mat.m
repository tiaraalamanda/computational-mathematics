%% Impor gambar bawah air tawar
clear,clc
gambar_1 = imread('D:\UNPAR\Semester 4\Metode Matematika A\Project UAS Kelompok A11\fresh-water.jpg'); %Impor gambar air tawar
ascii_ori_1 = uint8(gambar_1); %Representasi pixel gambar dalam matriks ke bilangan bulat 8 bit karena nilai maksimum pixel hanya sampai 255
r_ori_1=ascii_ori_1(:,:,1); % Ambil layar pertama (layar komponen merah) dari gambar 
g_ori_1=ascii_ori_1(:,:,2); % Ambil layar kedua (layar komponen hijau) dari gambar
b_ori_1=ascii_ori_1(:,:,3); % Ambil layar ketiga (layar komponen biru) dari gambar
ascii_edit_1 = uint8(gambar_1); % Buat lagi representasi pixel gambar dalam matriks untuk ditransformasi nilai-nilainya 
r_1=ascii_edit_1(:,:,1); % Ambil layar pertama (layar komponen merah) dari gambar yang akan ditransformasi
g_1=ascii_edit_1(:,:,2); % Ambil layar kedua (layar komponen hijau) dari gambar yang akan ditransformasi
b_1=ascii_edit_1(:,:,3); % Ambil layar ketiga (layar komponen biru) dari gambar yang akan ditransformasi
%% Transformasi dan Similarity Measurement
k = 2000; % nilai dari matriks konvolusi (dipilh sembarang)
c = [1/k 1/k 1/k;1/k 1/k 1/k;1/k 1/k 1/k]; % Matriks konvolusi
m_d = 150; % Manhattan Distance (dipilh sembarang) digunakan sebagai batasan agar hasil konvolusi tidak melenceng jauh dari gambar awal
d_e_sqr = 0; % Menampung nilai kuadrat dari Euclidian Distance yang digunakan sebagai ukuran perbedaan masing-masing nilai pixel sebelum dan setelah transformasi
j = 15; % Batasan(dipilh sembarang)digunakan sebagai batasan agar hasil transformasi tidak melenceng jauh dari gambar awal
[m,n]=size(r_1); % Menyimpan nilai banyak baris dan kolom dari layar merah
for u=0:m-1
    for v=0:n-1
        r_1(u+1,v+1)=r_ori_1(u+1,v+1)*(cos(2*pi*((u/m)+(v/n)))-sin(2*pi*((u/m)+(v/n)))); %Bagian penerapan T Fourier
        if r_1(u+1,v+1) > r_ori_1(u+1,v+1)
            % Karena nilai uint8 tidak bisa negatif, maka untuk menghitung
            % selish antar pixel harus nilai pixel yang lebih besar
            % dikurangi yang lebih kecil
            i = r_1(u+1,v+1) - r_ori_1(u+1,v+1); % Besar selisih antar pixel
            d_e_sqr = d_e_sqr + double(i)^2; % Nilai i tersebut ditampung, harus menggunakan double() agar bisa dikuadratkan 
        else
            i = r_ori_1(u+1,v+1)- r_1(u+1,v+1); % Besar selisih antar pixel
            d_e_sqr = d_e_sqr + double(i)^2; % Nilai i tersebut ditampung, harus menggunakan double() agar bisa dikuadratkan
        end
        if i > j
            % Jika selisih melebih batas yang ditentukan, maka
            % pixel itu tidak akan ditransformasi
            r_1(u+1,v+1) = r_ori_1(u+1,v+1);
        end
    end
end

r_1_c = conv2(r_1,c,'same'); % Melakukan konvolusi antara matriks gambar hasil transformasi dan matriks konvolusi
[m,n] = size(r_1); % Menyimpan nilai banyak baris dan kolom
for u=0:m-1
    for v=0:n-1
        if abs(double(r_1_c(u+1,v+1))-double(r_1(u+1,v+1))) > m_d
            % Jika selisih nilai pixel setelah konvolusi melebih batas yang ditentukan, maka
            % pixel itu akan diubah menjadi nilai pixel gambar semula
            r_1_c(u+1,v+1) = r_ori_1(u+1,v+1);
        end
    end
end

% Sama saja hanya untuk layar hijau
[m,n]=size(g_1);
for u=0:m-1
    for v=0:n-1
        g_1(u+1,v+1)=g_ori_1(u+1,v+1)*(cos(2*pi*((u/m)+(v/n)))-sin(2*pi*((u/m)+(v/n))));
        if g_1(u+1,v+1) > g_ori_1(u+1,v+1)
            i = g_1(u+1,v+1) - g_ori_1(u+1,v+1);
            d_e_sqr = d_e_sqr + double(i)^2;
        else
            i = g_ori_1(u+1,v+1)- g_1(u+1,v+1);
            d_e_sqr = d_e_sqr + double(i)^2;
        end
        if i > j
            g_1(u+1,v+1) = g_ori_1(u+1,v+1);
        end
    end
end

g_1_c = conv2(g_1,c,'same');
[m,n] = size(g_1_c);
for u=0:m-1
    for v=0:n-1
        if abs(double(g_1_c(u+1,v+1))-double(g_1(u+1,v+1))) > m_d
            g_1_c(u+1,v+1) = g_ori_1(u+1,v+1);
        end
    end
end

% Sama saja hanya untuk layar biru
[m,n]=size(b_1);
for u=0:m-1
    for v=0:n-1
        b_1(u+1,v+1)=b_ori_1(u+1,v+1)*(cos(2*pi*((u*(u/m)+(v/n)))-sin(2*pi*((u/m)+(v/n)))));
        if b_1(u+1,v+1) > b_ori_1(u+1,v+1)
            i = b_1(u+1,v+1) - b_ori_1(u+1,v+1);
            d_e_sqr = d_e_sqr + double(i)^2;
        else
            i = b_ori_1(u+1,v+1)- b_1(u+1,v+1);
            d_e_sqr = d_e_sqr + double(i)^2;
        end
        if i > j
            b_1(u+1,v+1) = b_ori_1(u+1,v+1);
        end
    end
end

b_1_c = conv2(b_1,c,'same');
[m,n] = size(b_1_c);
for u=0:m-1
    for v=0:n-1
        if abs(double(b_1_c(u+1,v+1))-double(b_1(u+1,v+1))) > m_d
            b_1_c(u+1,v+1) = b_ori_1(u+1,v+1);
        end
    end
end

rgbimage_1 = cat(3,r_1_c,g_1_c,b_1_c); %Menggabungkan ketiga layar menjadi satu gambar
d_e = sqrt(d_e_sqr) % Menampilkan nilai Euclidian Distance
%% Grafik perbandingan gambar 1
%Menampilkan gambar sebelum dan sesudah T Fourier disertai Histogram dari
%nilai pixel-pixelnya
figure;
subplot(2,2,1),imshow(gambar_1); 
title('Gambar 1 sebelum transformasi');
subplot(2,2,2),imshow(rgbimage_1);
title('Gambar 1 setelah transformasi');
subplot(2,2,3),imhist(gambar_1);
title('Histogram sebelum transformasi');
subplot(2,2,4),imhist(rgbimage_1);
title('Histogram setelah transformasi');
%Perhatikan nilai pixel-pixel yang setelah transformasi, yang
%nilai-nilainya rendah(gelap) menjadi berkurang sehingga gambar menjadi
%lebih terang
%% Impor gambar bawah air laut
% Sama saja hanya untuk gambar bawah air laut
clear,clc
gambar_2 = imread('D:\UNPAR\Semester 4\Metode Matematika A\Project UAS Kelompok A11\salt-water.jpg');
ascii_ori_2 = uint8(gambar_2);
r_ori_2=ascii_ori_2(:,:,1);
g_ori_2=ascii_ori_2(:,:,2);
b_ori_2=ascii_ori_2(:,:,3); 
ascii_edit_2 = uint8(gambar_2);
r_2=ascii_edit_2(:,:,1);
g_2=ascii_edit_2(:,:,2);
b_2=ascii_edit_2(:,:,3);
%% Transformasi dan Similarity Measurement
k = 2000;
c = [1/k 1/k 1/k;1/k 1/k 1/k;1/k 1/k 1/k];
m_d = 150;
d_e_sqr = 0;
j = 15;
[m,n]=size(r_2);
for u=0:m-1
    for v=0:n-1
        r_2(u+1,v+1)=r_ori_2(u+1,v+1)*(cos(2*pi*((u/m)+(v/n)))-sin(2*pi*((u/m)+(v/n))));
        if r_2(u+1,v+1) > r_ori_2(u+1,v+1)
            i = r_2(u+1,v+1) - r_ori_2(u+1,v+1);
            d_e_sqr = d_e_sqr + double(i)^2;
        else
            i = r_ori_2(u+1,v+1)- r_2(u+1,v+1);
            d_e_sqr = d_e_sqr + double(i)^2;
        end
        if i > j
            r_2(u+1,v+1) = r_ori_2(u+1,v+1);
        end
    end
end

r_2_c = conv2(r_2,c,'same');
[m,n] = size(r_2);
for u=0:m-1
    for v=0:n-1
        if abs(double(r_2_c(u+1,v+1))-double(r_2(u+1,v+1))) > m_d
            r_2_c(u+1,v+1) = r_ori_2(u+1,v+1);
        end
    end
end

[m,n]=size(g_2);
for u=0:m-1
    for v=0:n-1
        g_2(u+1,v+1)=g_ori_2(u+1,v+1)*(cos(2*pi*((u/m)+(v/n)))-sin(2*pi*((u/m)+(v/n))));
        if g_2(u+1,v+1) > g_ori_2(u+1,v+1)
            i = g_2(u+1,v+1) - g_ori_2(u+1,v+1);
            d_e_sqr = d_e_sqr + double(i)^2;
        else
            i = g_ori_2(u+1,v+1)- g_2(u+1,v+1);
            d_e_sqr = d_e_sqr + double(i)^2;
        end
        if i > j
            g_2(u+1,v+1) = g_ori_2(u+1,v+1);
        end
    end
end

g_2_c = conv2(g_2,c,'same');
[m,n] = size(g_2_c);
for u=0:m-1
    for v=0:n-1
        if abs(double(g_2_c(u+1,v+1))-double(g_2(u+1,v+1))) > m_d
            g_2_c(u+1,v+1) = g_ori_2(u+1,v+1);
        end
    end
end

[m,n]=size(b_2);
for u=0:m-1
    for v=0:n-1
        b_2(u+1,v+1)=b_ori_2(u+1,v+1)*(cos(2*pi*((u*(u/m)+(v/n)))-sin(2*pi*((u/m)+(v/n)))));
        if b_2(u+1,v+1) > b_ori_2(u+1,v+1)
            i = b_2(u+1,v+1) - b_ori_2(u+1,v+1);
            d_e_sqr = d_e_sqr + double(i)^2;
        else
            i = b_ori_2(u+1,v+1)- b_2(u+1,v+1);
            d_e_sqr = d_e_sqr + double(i)^2;
        end
        if i > j
            b_2(u+1,v+1) = b_ori_2(u+1,v+1);
        end
    end
end

b_2_c = conv2(b_2,c,'same');
[m,n] = size(b_2_c);
for u=0:m-1
    for v=0:n-1
        if abs(double(b_2_c(u+1,v+1))-double(b_2(u+1,v+1))) > m_d
            b_2_c(u+1,v+1) = b_ori_2(u+1,v+1);
        end
    end
end

rgbimage_2 = cat(3,r_2_c,g_2_c,b_2_c);
d_e = sqrt(d_e_sqr)
%% Grafik perbandingan gambar 2
figure;
subplot(2,2,1),imshow(gambar_2);
title('Gambar 2 sebelum transformasi');
subplot(2,2,2),imshow(rgbimage_2);
title('Gambar 2 setelah transformasi');
subplot(2,2,3),imhist(gambar_2);
title('Histogram sebelum transformasi');
subplot(2,2,4),imhist(rgbimage_2);
title('Histogram setelah transformasi');