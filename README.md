<table>
	<thead>
    	<tr>
      		<th style="text-align:center">日本語</th>
      		<th style="text-align:center"><a href="README_en.md">English</a></th>
    	</tr>
  	</thead>
</table>

### これは何? 
- [VSJ2025 Summer](https://sites.google.com/view/vsj2025summer/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0?authuser=0) にて発表したポスター (2p38) のサンプルコード。

### 提案手法の概説
- 本研究では、花弁組織構造から導出された断面モデルとKubelka-Munk理論に基づく励起蛍光シミュレーション手法を提案した。
- 既存のKubelka-Munk理論に蛍光項を追加することで拡張し、花弁内部の蛍光伝播のシミュレーションを可能とした。

### 環境構築
- Python 3.13
- [uv](https://docs.astral.sh/uv/) 

### 実行方法
```
uv install
uv run python linear_eq.py
```
### サンプルコードの出力
#### ① 蛍光項の入力値が0の場合
<img width="400" height="200" alt="nonf_led" src="https://github.com/user-attachments/assets/4ece92d5-c40e-43ec-a8cf-d060dfc4e310" />
<br/>
<img width="400" height="200" alt="nonf_d65" src="https://github.com/user-attachments/assets/2434fa56-4e17-43e7-ab13-6f47aade20a3" />


#### ② クマリンの蛍光波長をモデルとした理想的な蛍光色素のスペクトル情報を蛍光項の入力値として用いる場合
<img width="400" height="200" alt="Cm_led" src="https://github.com/user-attachments/assets/f57de3ce-b759-4667-a7ad-f33f3fa82632" />
<br/>
<img width="400" height="200" alt="Cm_d65" src="https://github.com/user-attachments/assets/47a3a369-b331-4386-bcd3-8648ddec300b" />


#### ③ クロロフィルaの蛍光波長をモデルとした理想的な蛍光色素のスペクトル情報を蛍光項の入力値として用いる場合
<img width="400" height="200" alt="cloro_led" src="https://github.com/user-attachments/assets/de390649-6573-4bb1-afcc-e155110a9017" />
<br/>
<img width="400" height="200" alt="cloro_d65" src="https://github.com/user-attachments/assets/0bc3d155-60b1-4709-804d-e7336b85977b" />

### 上記の出力の仮定
- 蛍光は吸収エネルギー＝発光エネルギーである。
- 再帰的蛍光は発生しない。
- 蛍光波長は吸収波長の逆相形となる。
- 簡略化のため、各波長は300～800nmの範囲内で11点を均一にサンプリングした。

### 提案した式
- 紫外光領域 (吸収)
  
<img width="317" height="76" alt="スクリーンショット 2025-09-13 14 17 42" src="https://github.com/user-attachments/assets/61d4ad97-aada-43e9-baa9-111fae4e96b2" />

- 可視光領域 (発光)
  
<img width="419" height="76" alt="スクリーンショット 2025-09-13 14 17 34" src="https://github.com/user-attachments/assets/1a02ddc7-7b42-4ac2-896a-72c9afdfd804" /></br>

吸収項には「-」項を、放射項には「+」項を既存の式に追加した。
