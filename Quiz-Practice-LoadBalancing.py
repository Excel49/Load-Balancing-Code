def dynamic_distribution(tasks, num_workers):
    """
    Menyimulasikan distribusi tugas secara dinamis (Load Balancing).
    Tugas selalu diberikan kepada pekerja dengan total beban (waktu) paling sedikit saat itu.
    """
    print(f"=== DYNAMIC DISTRIBUTION ===")
    print(f"Total Tugas: {len(tasks)} | Total Pekerja: {num_workers}\n")
    
    # Array untuk melacak total waktu pemrosesan yang sedang ditanggung setiap pekerja
    workers_load = [0] * num_workers
    
    # Simulasi eksekusi tugas satu per satu (dinamis)
    for index, task_time in enumerate(tasks):
        # 1. Mencari pekerja yang memiliki beban paling ringan saat ini
        available_worker = workers_load.index(min(workers_load))
        
        # 2. Mendistribusikan tugas ke pekerja tersebut
        workers_load[available_worker] += task_time
        
        # Penjelasan eksekusi setiap tugas (sesuai permintaan soal)
        print(f"[Eksekusi] Tugas ke-{index + 1} (butuh {task_time}s) -> Dialokasikan ke Pekerja {available_worker + 1}")
        print(f"           Beban Pekerja {available_worker + 1} sekarang menjadi {workers_load[available_worker]}s")

    print("\n=== Hasil Akhir ===")
    for i, load in enumerate(workers_load):
         print(f"Pekerja {i + 1} menyelesaikan seluruh tugas dalam: {load}s")
         
    # Expected Optimal Time adalah waktu dari pekerja yang selesai paling terakhir (makespan)
    expected_optimal_time = max(workers_load)
    
    print("-" * 50)
    print(f"[*] EXPECTED OPTIMAL TIME (Makespan): {expected_optimal_time} detik")
    print("-" * 50)
    
    return expected_optimal_time

if __name__ == "__main__":
    # Membuat data simulasi: 12 tugas dengan waktu penyelesaian acak 1-10 detik
    simulated_tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
    
    print(f"Daftar Waktu Tugas yang masuk antrean: {simulated_tasks}\n")
    
    # Menjalankan fungsi dengan asumsi 3 pekerja/core
    dynamic_distribution(simulated_tasks, num_workers=3)