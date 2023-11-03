# Tugas Eksperimen 1 DAA
## Merge Sort vs Two Pivot Block Quicksort (TPB Quicksort)

Nama: Andi Muhamad Dzaky Raihan <br>
NPM: 2106631412 <br>
Kode Asdos: 3 <br>

Perlu diperhatikan, data yang dihasilkan **berasal dari kode java**, bukan kode python. Selain itu, ada sedikit modifikasi di quicksort sehingga  quicksort dilakukan secara iteratif (behaviour dari rekursi dipertahankan melalui iterasi menggunakan stack). Terakhir, **ukuran Block** yang saya gunakan adalah **2^(floor(logn / 3) + 2)** . Saya ambil angka ini karena pada (Aumüller & Hass, 2019, 9) untuk data ukuran 226 ukuran blok yang optimal adalah 210.

Referensi:
* Aumüller, M., & Hass, N. (2019). Simple and Fast BlockQuicksort using Lomuto’s Partitioning Scheme. In 2019 Proceedings of the Twenty-First Workshop on Algorithm Engineering and Experiments (ALENEX) (pp. 15-26). Society for Industrial and Applied Mathematics. 10.1137/1.9781611975499.2