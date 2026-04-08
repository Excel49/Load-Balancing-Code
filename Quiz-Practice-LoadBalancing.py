

def static_uneven_distribution(tasks, num_workers):
    """
    Menyimulasikan distribusi tugas secara statis (Round-Robin) untuk tugas yang tidak merata (uneven).
    Menampilkan momen kapan seorang pekerja mencapai/melewati "Ideal Distribution".
    """
    print(f"=== STATIC UNEVEN DISTRIBUTION ===")
    print(f"Total Tugas: {len(tasks)} | Total Pekerja: {num_workers}\n")
    
    # Menghitung Ideal Distribution
    # Idealnya, jika tugas bisa dibagi rata sempurna, setiap pekerja akan mendapat beban ini.
    total_workload = sum(tasks)
    ideal_distribution = total_workload / num_workers
    
    print(f"Total Seluruh Beban Kerja: {total_workload} detik")
    print(f"[*] IDEAL DISTRIBUTION (Target Rata-rata): {ideal_distribution:.2f} detik per pekerja\n")
    
    workers_load = [0] * num_workers
    
    # Eksekusi secara statis (dibagi bergantian / Round-Robin)
    for index, task_time in enumerate(tasks):
        # 1. Menentukan pekerja secara statis berdasarkan urutan (index), bukan berdasarkan beban
        assigned_worker = index % num_workers
        
        # 2. Mendistribusikan tugas ke pekerja tersebut
        workers_load[assigned_worker] += task_time
        
        # Output Penjelasan Eksekusi
        print(f"[Eksekusi] Tugas ke-{index + 1} (beban {task_time}s) -> Dialokasikan secara statis ke Pekerja {assigned_worker + 1}")
        print(f"           Beban Pekerja {assigned_worker + 1} sekarang: {workers_load[assigned_worker]}s")
        
        # 3. Menunjukkan KAPAN kode mencapai/melewati Ideal Distribution (Sesuai permintaan soal)
        if workers_load[assigned_worker] >= ideal_distribution:
            print(f"           >>> [INFO] Pekerja {assigned_worker + 1} telah mencapai/melewati batas Ideal Distribution! <<<")

    print("\n=== Hasil Akhir Distribusi (Uneven / Tidak Merata) ===")
    for i, load in enumerate(workers_load):
         # Menampilkan hasil akhir yang kemungkinan besar tidak merata karena distribusinya statis
         print(f"Pekerja {i + 1} total beban: {load}s (Selisih dari ideal: {abs(load - ideal_distribution):.2f}s)")
         
    print("-" * 55)
    print(f"[*] IDEAL DISTRIBUTION POINT: {ideal_distribution:.2f} detik")
    print("-" * 55)

if __name__ == "__main__":

    simulated_tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Contoh beban tugas yang tidak merata (uneven)
    
    print(f"Daftar Waktu Tugas (Uneven): {simulated_tasks}\n")
    
    # Menjalankan fungsi dengan 3 pekerja
    static_uneven_distribution(simulated_tasks, num_workers=3)