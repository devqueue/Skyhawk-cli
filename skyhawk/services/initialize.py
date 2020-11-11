import os

def run():
    current_dir = os.getcwd()
    faces_dir = "skyhawk/facedata"
    bin_dir = "skyhawk/bin"
    face_path = os.path.join(current_dir,faces_dir)
    bin_path = os.path.join(current_dir,bin_dir)
    os.makedirs(face_path, exist_ok=True)
    os.makedirs(bin_path, exist_ok=True)
    with open('skyhawk/bin/Attendance.csv', 'w') as file:
        HEADER = "Name, Date, Time, Day "
        file.write(HEADER)
    print('\n')
    print("             Welcome to skyhawk! Auto-attandance cli tool      ")
    print('''
                                                                                                        
                                   -://-`                                               
                                 /dNMMMNmo`                                             
                                +MMMy+sNMMy                                             
                                hMMm`  yMMN`                                            
                      .--.`     :NMMmhdMMNo      .-:-`                                  
                    :hNNNNd/     -sdMMMmy:     :hNNNNd+                                 
                   -NMd::yMM:     .sNMMh-     .NMd:-yMM/                                
                   -NMd::hMM:    :mMMMMMN+    .NMm::yMM/                                
            `.`     :hNNNMm/     :MMMMMMMo     :dMMNNd+     `..                         
          -ymdmh:    `.:mMNho.   `mMMMMMM-   `+ymMN+.`    .yddmh/                       
         `mMo-+MN.     yMMMMMy    sMMMMMd    +MMMMMd`     dMs-/NN-                      
          yMdohMd`     +NMMMMm    -MMMMM+    yMMMMMs`    `yMdoyMd`                      
          `:oysNmdh/    /NMMMM.    dMMMN.   `mMMMMs`   :hdmMyys/`                       
              .NMMMN/    /NMMM/    +MMMy    -MMMMo    -mMMMM/                           
              `/dMMMN/    :mMMy    .NMM:    +MMN+    -mMMMmo`                           
                `/dMMN:    -mMm`    hMm`    yMN/    .mMMm+.                             
                  `/hNm-    -mM.    /Ms    `mN/    .dMd+`                               
                     :hd-    .d/    `m-    .m:    `hd/`                                 
                      `:o`    ./     :     :-    `+d`                                    
                                                                                                     
    '''
    )
    print("Data directories initialized sucessfully")
