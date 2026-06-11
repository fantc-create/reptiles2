html_api_content = """<!DOCTYPE html>
<html lang="zh-HK">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>學校生物角 - 跨設備雲端自動同步護理系統 (GitHub API版)</title>
    <style>
        * { box-sizing: border-box; }
        body {
            font-family: "Microsoft JhengHei", "PingFang HK", "Helvetica Neue", Arial, sans-serif;
            background-color: #f3f6f5;
            color: #2c3e50;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }
        .header-banner {
            background-color: #1b5e20;
            color: white;
            text-align: center;
            padding: 30px 15px;
        }
        .header-banner h1 { margin: 0; font-size: 22pt; font-weight: bold; }
        .header-banner p { margin: 10px 0 0 0; font-size: 11pt; opacity: 0.9; }
        
        .nav-tabs {
            background-color: #e8f5e9;
            text-align: center;
            padding: 10px 0;
            border-bottom: 2px solid #c8e6c9;
        }
        .tab-btn {
            display: inline-block;
            background-color: #ffffff;
            color: #2e7d32;
            padding: 12px 24px;
            font-size: 11pt;
            font-weight: bold;
            border: 2px solid #a5d6a7;
            border-radius: 20px;
            margin: 5px;
            cursor: pointer;
            text-decoration: none;
        }
        .tab-btn.active {
            background-color: #2e7d32;
            color: white;
            border-color: #2e7d32;
        }
        .container { max-width: 1000px; margin: 20px auto; padding: 0 15px; }
        .section-panel {
            display: none;
            background-color: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 30px;
        }
        .section-panel.active { display: block; }
        h2 {
            color: #1b5e20; font-size: 15pt; border-left: 5px solid #2e7d32;
            padding-left: 10px; margin-top: 0; margin-bottom: 20px;
        }
        .info-block {
            background-color: #f8faf9; border: 1px solid #e0e6e4;
            border-radius: 8px; padding: 15px; margin-bottom: 25px;
        }
        .info-row { margin-bottom: 12px; }
        .info-row label { display: inline-block; width: 100px; font-weight: bold; }
        .info-row input[type="text"], .info-row input[type="date"] {
            width: 220px; padding: 8px; border: 1px solid #ccc; border-radius: 4px; font-size: 10.5pt;
        }
        table { width: 100%; border-collapse: collapse; margin-bottom: 25px; }
        th, td { border: 1px solid #dcdcdc; padding: 12px 10px; text-align: left; font-size: 10.5pt; }
        th { background-color: #f1f5f2; color: #2e7d32; font-weight: bold; text-align: center; }
        .animal-title-col { background-color: #f9fbf9; font-weight: bold; text-align: center; width: 14%; }
        .check-group { display: block; margin-bottom: 8px; cursor: pointer; }
        .qty-box { width: 60px; padding: 4px; margin-left: 5px; border: 1px solid #ccc; border-radius: 3px; text-align: center; }
        .na-cell { color: #95a5a6; font-style: italic; text-align: center; background-color: #fafafa; }
        
        .btn-container { text-align: center; margin-top: 25px; }
        .action-btn {
            background-color: #2e7d32; color: white; font-size: 12pt; font-weight: bold;
            padding: 14px 35px; border: none; border-radius: 8px; cursor: pointer;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .action-btn:disabled { background-color: #a5d6a7; cursor: not-allowed; }
        .reset-btn {
            background-color: #e0e0e0; color: #333; font-size: 10.5pt;
            padding: 10px 20px; border: none; border-radius: 6px; cursor: pointer; margin-right: 15px;
        }
        .iframe-container { width: 100%; height: 650px; border: 1px solid #dcdcdc; border-radius: 8px; overflow: hidden; }
        iframe { width: 100%; height: 100%; border: none; }

        @media (max-width: 768px) {
            table, thead, tbody, th, td, tr { display: block; width: 100%; }
            thead { display: none; }
            tr { border: 2px solid #2e7d32; border-radius: 10px; margin-bottom: 20px; background-color: #ffffff; }
            td { border: none; border-bottom: 1px solid #f0f0f0; padding: 12px 15px; }
            td.animal-title-col { background-color: #2e7d32; color: white; font-size: 13pt; text-align: center; }
            td:not(.animal-title-col)::before {
                content: attr(data-label); display: block; font-weight: bold; color: #2e7d32;
                font-size: 9.5pt; margin-bottom: 6px; border-bottom: 1px dashed #e8f5e9; padding-bottom: 3px;
            }
            .na-cell { display: none; }
            .info-row label { display: block; margin-bottom: 5px; }
            .info-row input[type="text"], .info-row input[type="date"] { width: 100%; }
        }
    </style>
</head>
<body>

    <div class="header-banner">
        <h1>🐾 生物角日常護理系統</h1>
        <p>GitHub 託管 × Google API 跨手機自動同步版</p>
    </div>

    <div class="nav-tabs">
        <div class="tab-btn active" id="tab1-btn" onclick="switchTab(1)">✏️ 填寫護理表格</div>
        <div class="tab-btn" id="tab2-btn" onclick="switchTab(2)">📋 歷史紀錄大看板</div>
    </div>

    <div class="container">
        <div id="panel-1" class="section-panel active">
            <h2>日常護理核對登記</h2>
            <div class="info-block">
                <div class="info-row">
                    <label for="studentName">負責學生：</label>
                    <input type="text" id="studentName" placeholder="請輸入姓名（例如：張同學）">
                </div>
                <div class="info-row">
                    <label for="careDate">填寫日期：</label>
                    <input type="date" id="careDate">
                </div>
            </div>

            <table id="careTable">
                <thead>
                    <tr>
                        <th>生物名稱</th>
                        <th>📌 餵食狀況</th>
                        <th>💧 保濕 / 更換飲水</th>
                        <th>💩 排泄與脫皮</th>
                        <th>🔒 離開前鎖缸</th>
                        <th>⚖️ 體重磅重</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="animal-title-col">🦗 蟋蟀</td>
                        <td data-label="📌 餵食狀況"><label class="check-group"><input type="checkbox" value="餵食飼料" class="item-cb"> 餵食專用飼料</label></td>
                        <td data-label="💧 保濕 / 更換飲水" class="na-cell">不適用</td>
                        <td data-label="💩 排泄與脫皮"><label class="check-group"><input type="checkbox" value="清理排泄物" class="item-cb"> 清理排泄物</label></td>
                        <td data-label="🔒 離開前鎖缸" class="na-cell">不適用</td>
                        <td data-label="⚖️ 體重磅重" class="na-cell">不適用</td>
                    </tr>
                    <tr>
                        <td class="animal-title-col">🦎 變色龍</td>
                        <td data-label="📌 餵食狀況"><label class="check-group"><input type="checkbox" value="餵食蟋蟀" class="item-cb" data-has-qty="true"> 餵食蟋蟀 <input type="number" class="qty-box" min="0" placeholder="幾隻"> 隻</label></td>
                        <td data-label="💧 保濕 / 更換飲水"><label class="check-group"><input type="checkbox" value="全缸噴水保濕" class="item-cb"> 全缸噴水保濕</label></td>
                        <td data-label="💩 排泄與脫皮"><label class="check-group"><input type="checkbox" value="清理排泄物" class="item-cb"> 清理排泄物</label></td>
                        <td data-label="🔒 離開前鎖缸"><label class="check-group"><input type="checkbox" value="確認鎖好缸門" class="item-cb"> 確認鎖好缸門</label></td>
                        <td data-label="⚖️ 體重磅重"><label class="check-group"><input type="checkbox" value="每兩週磅重完成" class="item-cb"> 每兩週磅重完成</label></td>
                    </tr>
                    <tr>
                        <td class="animal-title-col">🐍 球蟒</td>
                        <td data-label="📌 餵食狀況"><label class="check-group"><input type="checkbox" value="餵食乳鼠" class="item-cb" data-has-qty="true"> 餵食乳鼠 <input type="number" class="qty-box" min="0" placeholder="幾隻"> 隻</label></td>
                        <td data-label="💧 保濕 / 更換飲水"><label class="check-group"><input type="checkbox" value="更換乾淨飲水" class="item-cb"> 更換乾淨飲水</label></td>
                        <td data-label="💩 排泄與脫皮"><label class="check-group"><input type="checkbox" value="清理排泄物" class="item-cb"> 清理排泄物</label></td>
                        <td data-label="🔒 離開前鎖缸"><label class="check-group"><input type="checkbox" value="確認鎖好鎖頭" class="item-cb"> 確認鎖好鎖頭</label></td>
                        <td data-label="⚖️ 體重磅重"><label class="check-group"><input type="checkbox" value="每兩週磅重完成" class="item-cb"> 每兩週磅重完成</label></td>
                    </tr>
                    <tr>
                        <td class="animal-title-col">🌱 植物</td>
                        <td data-label="📌 餵食狀況" class="na-cell">不適用</td>
                        <td data-label="💧 保濕 / 更換飲水"><label class="check-group"><input type="checkbox" value="全株葉面噴水保濕" class="item-cb"> 全株葉面噴水保濕</label></td>
                        <td data-label="💩 排泄與脫皮" class="na-cell">不適用</td>
                        <td data-label="🔒 離開前鎖缸" class="na-cell">不適用</td>
                        <td data-label="⚖️ 體重磅重" class="na-cell">不適用</td>
                    </tr>
                </tbody>
            </table>

            <div class="btn-container">
                <button type="button" class="reset-btn" onclick="resetCheckboxes()">清空重填</button>
                <button type="button" class="action-btn" id="submitBtn" onclick="uploadDataViaAPI()">🎉 填好了！一鍵同步到雲端</button>
            </div>
        </div>

        <div id="panel-2" class="section-panel">
            <h2>☁️ 全班共用歷史紀錄大看板</h2>
            <div class="iframe-container">
                <iframe id="sheetIframe" src="https://docs.google.com/spreadsheets/your-sheet-url-here/pubhtml?widget=true&headers=false"></iframe>
            </div>
        </div>
    </div>

    <script>
        // =========================================================================
        // 🛠️ 老師設定專區：請替換成您在 Google Apps Script 部署得到的網頁應用程式網址
        // =========================================================================
        const API_URL = "https://script.google.com/macros/s/your-apps-script-id-here/exec";
        const GOOG_SHEET_URL = "https://docs.google.com/spreadsheets/your-sheet-url-here/pubhtml?widget=true&headers=false";
        // =========================================================================

        document.addEventListener("DOMContentLoaded", function() {
            document.getElementById("careDate").value = new Date().toISOString().split('T')[0];
            if (GOOG_SHEET_URL && GOOG_SHEET_URL.indexOf("your-sheet-url") === -1) {
                document.getElementById("sheetIframe").src = GOOG_SHEET_URL;
            }
        });

        function switchTab(tabNum) {
            document.querySelectorAll(".tab-btn").forEach(btn => btn.classList.remove("active"));
            document.querySelectorAll(".section-panel").forEach(panel => panel.classList.remove("active"));
            document.getElementById("tab" + tabNum + "-btn").classList.add("active");
            document.getElementById("panel-" + tabNum).classList.add("active");
            
            if (tabNum === 2 && GOOG_SHEET_URL && GOOG_SHEET_URL.indexOf("your-sheet-url") === -1) {
                document.getElementById("sheetIframe").src = GOOG_SHEET_URL + "&cachebust=" + new Date().getTime();
            }
        }

        function resetCheckboxes() {
            if(confirm("確定要清空嗎？")) {
                document.querySelectorAll(".item-cb").forEach(cb => cb.checked = false);
                document.querySelectorAll(".qty-box").forEach(box => box.value = "");
            }
        }

        function uploadDataViaAPI() {
            const studentName = document.getElementById("studentName").value.trim();
            const careDate = document.getElementById("careDate").value;

            if (!studentName) {
                alert("請先填寫『負責學生姓名』！");
                document.getElementById("studentName").focus();
                return;
            }

            let summaryText = "";
            let checkedCount = 0;
            const rows = document.getElementById("careTable").getElementsByTagName("tbody")[0].getElementsByTagName("tr");

            for (let i = 0; i < rows.length; i++) {
                const row = rows[i];
                const animalName = row.getElementsByClassName("animal-title-col")[0].innerText;
                const checkboxes = row.querySelectorAll(".item-cb:checked");

                if (checkboxes.length > 0) {
                    let animalActions = [];
                    checkboxes.forEach(cb => {
                        let actionStr = cb.value;
                        if (cb.getAttribute("data-has-qty") === "true") {
                            const qtyInput = cb.parentElement.querySelector(".qty-box");
                            if (qtyInput && qtyInput.value.trim() !== "") {
                                actionStr += "(" + qtyInput.value.trim() + "隻/份)";
                            }
                        }
                        animalActions.push(actionStr);
                    });
                    summaryText += "【" + animalName + "】 " + animalActions.join("、") + "\\n";
                    checkedCount++;
                }
            }

            if (checkedCount === 0) {
                alert("請至少勾選一項護理項目！");
                return;
            }

            if (API_URL.indexOf("your-apps-script-id-here") !== -1) {
                alert("❌ 偵測到尚未設定真正的 API_URL！請先用記事本修改程式碼中的 API 網址再上傳至 GitHub。");
                return;
            }

            const btn = document.getElementById("submitBtn");
            btn.innerText = "⏳ 雲端同步中...";
            btn.disabled = true;

            // 打包發送至 Google Apps Script API
            fetch(API_URL, {
                method: "POST",
                headers: { "Content-Type": "text/plain;charset=utf-8" },
                body: JSON.stringify({
                    studentName: studentName,
                    careDetails: "日期：" + careDate + "\\n" + summaryText
                })
            })
            .then(res => res.json())
            .then(res => {
                if(res.status === "success") {
                    alert("🎉 數據已直接射入 Google 雲端帳本！下一位同學隨時可刷新查看。");
                    document.querySelectorAll(".item-cb").forEach(cb => cb.checked = false);
                    document.querySelectorAll(".qty-box").forEach(box => box.value = "");
                } else {
                    alert("⚠️ 雲端接收異常：" + res.message);
                }
            })
            .catch(err => {
                console.error(err);
                alert("❌ 連線失敗！請確認 Google Apps Script 的權限是否設為『所有人(Anyone)』。");
            })
            .finally(() => {
                btn.innerText = "🎉 填好了！一鍵同步到雲端";
                btn.disabled = false;
            });
        }
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_api_content)
print("index.html created successfully.")