'''
1. 長短期記憶模型 (Long Short-Term Memory, LSTM) 
    為了解決 RNN 的問題(梯度爆炸/梯度消失)，LSTM 因此誕生。
    LSTM 通過門(Gates)，允許網路有選擇性的保留或丟棄信息，使 LSTM 能夠記住長時間的重要信息，並保持訓練的穩定性。


2. LSTM 結構
    LSTM 引入了一個稱為狀態保存層(Cell State)以及三種控制信息流動的門(GATE) 

    1. 狀態保存層(Cell State)：
        狀態保存層是LSTM 中的一條「關鍵信息通道」，允許信息在每個時間之間幾乎不受干擾的傳遞。
        它使得信息能夠長時間在網路中保持流通，而不會像 RNN 那樣容易受到梯度消失的影響。
        細胞裡有一個狀態保存層(Cell State)和一個隱藏狀態(Hidden State)，胞狀態保存長期記憶，而隱藏狀態就和RNN一樣用於當前時間步之前的記憶(短期)。
            
            1. 狀態保存層(Cell State, Ct)：用來保存長期記憶。
            2. 隱藏狀態(Hidden State, ht)：用來處理和保存當前時間步以及過去幾個時間步的短期記憶。
            
        
    2. 遺忘門(Forget Gate)：
        遺忘門决定 LSTM 在上一時間步狀態保存層 C(t-1) 需要「忘記」多少的記憶。
        遺忘門會根據當前的輸入 x(t) 和上一個時間步的隱藏狀態 h(t-1) 來計算0~1的值。值越接近 0，意味著越多的信息會被遺忘；值越接近 1，意味著更多的信息會被保留。

        遺忘門的輸出 f(t) = Sigmoid函數 * ( 遺忘門的權重矩陣 Wf @ [上一個時間步的隱藏狀態 h(t-1), 當前時間步的輸入x(t)] + 遺忘門的bias)
            1. f(t)：表示每個狀態保存層保留的比例  
            2. Sigmoid：將輸出的範圍壓縮到[0, 1]
            3. Wf：，將隱藏狀態和輸入進行線性變換
            4. [h(t-1), x(t)]：上一個時間步的隱藏狀態和當前的輸入，將它們拼接成一個向量
            
    
    3. 輸入門(Input Gate)：
        輸入門控制應該將多少新信息加入到狀態保存層中。分為兩部分：一個是控制引入多少新信息，另一個是生成這些新信息。
            
            1. 輸入門開關值：
                i(t) = Sigmoid * (Wi @ [h(t-1), x(t)] + bias)，與遺忘門公式相似，用來決定新信息應該引入多少。

            2. 候選記憶：
                C(t) = tanh 函數 * (Wc @ [h(t-1), x(t)] + bias) 
                    1. C(t)：候選記憶，是一個範圍在[-1, 1]之間的值，準備進入狀態保存層。
                    2. tanh(雙曲函數)：Tanh 函數，將結果壓縮到 [-1, 1]之間                    
                    3. Wc： 候選記憶的權重矩陣，用來線性變換當前的輸入x(t)和上一個隱藏狀態h(t-1)
                    

    4. 輸出門(Output Gate)：
        決定 LSTM 在當前時間步的最終輸出(即為隱藏狀態h(t))，LSTM 會根據當前的狀態保存層 C(t) 和當前輸入 x(t) 計算隱藏狀態。

            1.  輸出門開關值，決定輸出多少記憶(信息狀態保存層)：
                O(t) = Sigmoid (Wo @ [h(t-1), x(t)] + bias)
                    1. O(t)：值在[0, 1]，決定記憶單元的內容應該輸出多少。
                    2. Wo：輸出門的權重矩陣，用來將上一個隱藏狀態和當前的輸入經過線性變換得到輸出。

            2. 最終輸出(隱藏狀態)：
                ht = Ot @ tanh(Ct)
                    1. ht：當前時間步的最終輸出(隱藏狀態)，LSTM的輸出，也是下一個時間步的輸入。
                    2. tanh(Ct)：對當前的狀態保存層狀態 Ct 使用 Tanh函數，將狀態保存層的值壓縮到[-1, 1]

                
    3. LSTM 優勢
        LSTM 的三個門使網路能夠動態調整信息流，狀態保存層可以跨越多個時間步保持關鍵信息。
        這使得它能夠處理長序列數據，而不會像普通 RNN 那樣容易忘記早期的信息。有效緩解 RNN 在反向傳播中的梯度消失問題。
'''