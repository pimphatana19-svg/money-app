```html
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Store & Savings App 💖</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/js/all.min.js"></script>
    <style>
        * {
            font-family: 'Kanit', sans-serif;
        }
        body {
            background-color: #FFF0F5;
            color: #4A4A4A;
        }
        .pastel-card {
            background: #FFFFFF;
            border-radius: 20px;
            box-shadow: 0 10px 25px -5px rgba(255, 182, 193, 0.3), 0 8px 10px -6px rgba(255, 182, 193, 0.2);
            border: 2px solid #FFF0F5;
        }
        .btn-pastel {
            background-color: #FFB6C1;
            color: #FFFFFF;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(255, 182, 193, 0.5);
        }
        .btn-pastel:hover {
            background-color: #FF69B4;
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(255, 105, 180, 0.4);
        }
        .text-pastel-heading {
            color: #D87093;
        }
        .border-pastel {
            border-color: #FFB6C1;
        }
        .bg-pastel-soft {
            background-color: #FFF5F7;
        }
        .tab-btn.active {
            background-color: #FFB6C1;
            color: #FFFFFF;
            font-weight: 600;
        }
        /* Custom scrollbar for tables */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #FFF0F5;
        }
        ::-webkit-scrollbar-thumb {
            background: #FFB6C1;
            border-radius: 10px;
        }
    </style>
</head>
<body class="min-h-screen pb-12">

    <header class="bg-white border-b border-pink-100 sticky top-0 z-50 shadow-sm">
        <div class="max-w-5xl mx-auto px-4 py-3 flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-full bg-pink-100 flex items-center justify-center text-pink-500 text-xl font-bold">
                    🌸
                </div>
                <div>
                    <h1 class="text-xl font-bold text-pastel-heading leading-tight">Store & Savings</h1>
                    <p class="text-xs text-pink-400">ระบบออมเงิน & จัดการร้านค้าพาสเทล 💖</p>
                </div>
            </div>
            <button onclick="resetDataPrompt()" class="text-xs bg-pink-50 hover:bg-pink-100 text-pink-500 px-3 py-1.5 rounded-full transition">
                <i class="fa-solid fa-rotate-right mr-1"></i> รีเซ็ตข้อมูล
            </button>
        </div>
    </header>

    <main class="max-w-5xl mx-auto px-4 mt-6">
        <nav class="flex rounded-2xl bg-white p-1.5 shadow-sm border border-pink-100 mb-6 overflow-x-auto">
            <button onclick="switchSystem('savings')" id="nav-savings" class="tab-btn flex-1 min-w-[130px] py-2.5 px-3 rounded-xl text-sm font-medium text-gray-500 flex items-center justify-center space-x-2 transition">
                <span>💖</span> <span>ระบบออมเงิน</span>
            </button>
            <button onclick="switchSystem('grocery')" id="nav-grocery" class="tab-btn flex-1 min-w-[130px] py-2.5 px-3 rounded-xl text-sm font-medium text-gray-500 flex items-center justify-center space-x-2 transition">
                <span>🧺</span> <span>ร้านขายของชำ</span>
            </button>
            <button onclick="switchSystem('luxury')" id="nav-luxury" class="tab-btn flex-1 min-w-[130px] py-2.5 px-3 rounded-xl text-sm font-medium text-gray-500 flex items-center justify-center space-x-2 transition">
                <span>💎</span> <span>ร้านของฟุ่มเฟือย</span>
            </button>
        </nav>

        <section id="section-savings" class="space-y-6">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 bg-white p-6 rounded-2xl border border-pink-100 shadow-sm">
                <div>
                    <h2 class="text-2xl font-bold text-pastel-heading flex items-center gap-2">
                        <span>💖</span> ระบบคำนวณการออมเงิน 🐽
                    </h2>
                    <p class="text-sm text-gray-500 mt-1">วางแผนเป้าหมายการออม คำนวณระยะเวลา และจัดการเงินกลุ่ม/เดี่ยว</p>
                </div>
                <button onclick="openModal('modal-add-savings')" class="btn-pastel px-5 py-2.5 rounded-xl text-sm font-semibold flex items-center gap-2 w-full md:w-auto justify-center">
                    <i class="fa-solid fa-plus"></i> เพิ่มกระปุกออมเงิน
                </button>
            </div>

            <!-- Sub Tabs for Savings -->
            <div id="savings-cards-container" class="grid grid-cols-1 md:grid-cols-2 gap-5">
                <!-- Dynamic Savings Cards Will Render Here -->
            </div>
        </section>

        <section id="section-store" class="space-y-6 hidden">
            <div class="bg-white p-6 rounded-2xl border border-pink-100 shadow-sm flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
                <div>
                    <h2 id="store-title" class="text-2xl font-bold text-pastel-heading flex items-center gap-2">
                        <!-- Dynamic Store Title -->
                    </h2>
                    <p class="text-sm text-gray-500 mt-1">บันทึกรายการขาย และวิเคราะห์สถิติกำไรขายดี</p>
                </div>
                <div class="flex rounded-xl bg-pink-50 p-1 w-full md:w-auto">
                    <button onclick="switchStoreSubTab('record')" id="subnav-record" class="flex-1 md:flex-initial px-4 py-2 rounded-lg text-xs font-semibold transition text-pink-600 bg-white shadow-sm">
                        📝 บันทึกการขาย
                    </button>
                    <button onclick="switchStoreSubTab('analytics')" id="subnav-analytics" class="flex-1 md:flex-initial px-4 py-2 rounded-lg text-xs font-semibold transition text-gray-500">
                        📊 สถิติ & วิเคราะห์
                    </button>
                </div>
            </div>

            <!-- Sub Tab 1: Record Sales & History Table -->
            <div id="store-tab-record" class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <!-- Sales Entry Form -->
                <div class="pastel-card p-6 h-fit">
                    <h3 class="text-lg font-bold text-pastel-heading mb-4 flex items-center gap-2">
                        <i class="fa-solid fa-cart-plus"></i> บันทึกรายการขายใหม่
                    </h3>
                    <form id="form-add-sale" onsubmit="handleAddSale(event)" class="space-y-4">
                        <div>
                            <label class="block text-xs font-medium text-gray-600 mb-1">วันที่ขาย</label>
                            <input type="date" id="sale-date" required class="w-full px-3 py-2 border border-pink-200 rounded-xl focus:outline-none focus:border-pink-400 text-sm bg-pastel-soft">
                        </div>
                        <div>
                            <label class="block text-xs font-medium text-gray-600 mb-1">เวลาขาย (ชั่วโมง 0-23 น.)</label>
                            <input type="number" id="sale-time" min="0" max="23" required class="w-full px-3 py-2 border border-pink-200 rounded-xl focus:outline-none focus:border-pink-400 text-sm bg-pastel-soft">
                        </div>
                        <div>
                            <label class="block text-xs font-medium text-gray-600 mb-1">หมวดหมู่สินค้า</label>
                            <input type="text" id="sale-category" placeholder="เช่น เครื่องดื่ม, ของใช้" required class="w-full px-3 py-2 border border-pink-200 rounded-xl focus:outline-none focus:border-pink-400 text-sm bg-pastel-soft">
                        </div>
                        <div>
                            <label class="block text-xs font-medium text-gray-600 mb-1">ชื่อสินค้า</label>
                            <input type="text" id="sale-name" placeholder="เช่น ชานมมุก, กระเป๋า" required class="w-full px-3 py-2 border border-pink-200 rounded-xl focus:outline-none focus:border-pink-400 text-sm bg-pastel-soft">
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-medium text-gray-600 mb-1">ต้นทุน (บาท)</label>
                                <input type="number" step="0.01" id="sale-cost" min="0" required class="w-full px-3 py-2 border border-pink-200 rounded-xl focus:outline-none focus:border-pink-400 text-sm bg-pastel-soft">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-gray-600 mb-1">ราคาขาย (บาท)</label>
                                <input type="number" step="0.01" id="sale-price" min="0" required class="w-full px-3 py-2 border border-pink-200 rounded-xl focus:outline-none focus:border-pink-400 text-sm bg-pastel-soft">
                            </div>
                        </div>
                        <button type="submit" class="w-full btn-pastel py-2.5 rounded-xl text-sm font-semibold mt-2 flex items-center justify-center gap-2">
                            🛒 บันทึกรายการขาย
                        </button>
                    </form>
                </div>

                <!-- Sales History Table -->
                <div class="pastel-card p-6 lg:col-span-2 flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-center mb-4">
                            <h3 class="text-lg font-bold text-pastel-heading flex items-center gap-2">
                                <i class="fa-solid fa-list-check"></i> รายการขายทั้งหมด
                            </h3>
                            <span id="sales-count-badge" class="bg-pink-100 text-pink-600 text-xs px-3 py-1 rounded-full font-medium">0 รายการ</span>
                        </div>
                        <div class="overflow-x-auto max-h-[420px] overflow-y-auto">
                            <table class="w-full text-left border-collapse text-sm">
                                <thead>
                                    <tr class="border-b border-pink-100 text-pink-500 bg-pink-50/50 sticky top-0">
                                        <th class="p-3">วันที่/เวลา</th>
                                        <th class="p-3">หมวดหมู่</th>
                                        <th class="p-3">สินค้า</th>
                                        <th class="p-3 text-right">ต้นทุน</th>
                                        <th class="p-3 text-right">ราคาขาย</th>
                                        <th class="p-3 text-right">กำไร</th>
                                        <th class="p-3 text-center">จัดการ</th>
                                    </tr>
                                </thead>
                                <tbody id="sales-table-body" class="divide-y divide-pink-50">
                                    <!-- Dynamic Rows -->
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Sub Tab 2: Analytics Dashboard -->
            <div id="store-tab-analytics" class="space-y-6 hidden">
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4" id="analytics-metrics-grid">
                    <!-- Dynamic Analytics Cards -->
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <!-- Stock Recommendation Card -->
                    <div class="pastel-card p-6">
                        <h3 class="text-lg font-bold text-pastel-heading mb-3 flex items-center gap-2">
                            <span>🛍️</span> สินค้าแนะนำให้สั่งสต็อกเพิ่ม
                        </h3>
                        <p class="text-xs text-gray-500 mb-4">วิเคราะห์จากยอดขายและความนิยมสูงสุดเรียงตามลำดับ</p>
                        <div id="stock-recommendations-list" class="space-y-3">
                            <!-- Dynamic Stock Recs -->
                        </div>
                    </div>

                    <!-- Additional Summary Info -->
                    <div class="pastel-card p-6">
                        <h3 class="text-lg font-bold text-pastel-heading mb-3 flex items-center gap-2">
                            <span>📊</span> สรุปภาพรวมร้านค้า
                        </h3>
                        <div id="analytics-summary-box" class="space-y-3 text-sm">
                            <!-- Dynamic Summary Info -->
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <div id="modal-add-savings" class="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
        <div class="pastel-card max-w-md w-full p-6 animate-fade-in relative max-h-[90vh] overflow-y-auto">
            <button onclick="closeModal('modal-add-savings')" class="absolute top-4 right-4 text-gray-400 hover:text-pink-500 text-lg">
                <i class="fa-solid fa-xmark"></i>
            </button>
            <h3 class="text-xl font-bold text-pastel-heading mb-4 flex items-center gap-2">
                ✨ สร้างกระปุกออมเงินใหม่
            </h3>
            <form onsubmit="handleAddSavingsGoal(event)" class="space-y-4">
                <div>
                    <label class="block text-xs font-medium text-gray-600 mb-1">ตั้งชื่อกระปุกออมเงิน</label>
                    <input type="text" id="savings-name" placeholder="เช่น กระปุกไปเที่ยวเกาหลี" required class="w-full px-3 py-2 border border-pink-200 rounded-xl focus:outline-none focus:border-pink-400 text-sm bg-pastel-soft">
                </div>
                <div>
                    <label class="block text-xs font-medium text-gray-600 mb-1">จำนวนคนที่ร่วมออม (คน)</label>
                    <input type="number" id="savings-n" min="1" value="1" required onchange="calculateSavingsPreview()" class="w-full px-3 py-2 border border-pink-200 rounded-xl focus:outline-none focus:border-pink-400 text-sm bg-pastel-soft">
                </div>
                <div>
                    <label class="block text-xs font-medium text-gray-600 mb-1">รายชื่อสมาชิก (คั่นด้วยจุลภาค ,)</label>
                    <input type="text" id="savings-members" placeholder="เช่น ม่อน, เนเน่" required class="w-full px-3 py-2 border border-pink-200 rounded-xl focus:outline-none focus:border-pink-400 text-sm bg-pastel-soft">
                </div>
                <div>
                    <label class="block text-xs font-medium text-gray-600 mb-1">ความถี่กี่วันออมที (เช่น 1=ทุกวัน, 7=ทุกสัปดาห์)</label>
                    <input type="number" id="savings-w" min="1" value="1" required onchange="calculateSavingsPreview()" class="w-full px-3 py-2 border border-pink-200 rounded-xl focus:outline-none focus:border-pink-400 text-sm bg-pastel-soft">
                </div>

                <div class="bg-pink-50 p-3 rounded-xl border border-pink-100">
                    <label class="block text-xs font-semibold text-pastel-heading mb-2">รูปแบบการตั้งเป้าหมาย:</label>
                    <div class="space-y-2 text-xs">
                        <label class="flex items-center space-x-2 cursor-pointer">
                            <input type="radio" name="savings-mode" value="target" checked onchange="toggleSavingsModeUI()" class="accent-pink-500">
                            <span>กำหนดเงินเป้าหมายรวม (คำนวณเงินออมต่อครั้ง)</span>
                        </label>
                        <label class="flex items-center space-x-2 cursor-pointer">
                            <input type="radio" name="savings-mode" value="days" onchange="toggleSavingsModeUI()" class="accent-pink-500">
                            <span>กำหนดจำนวนวันออม (คำนวณเป้าหมายรวม)</span>
                        </label>
                    </div>
                </div>

                <div id="savings-input-mode-target">
                    <label class="block text-xs font-medium text-gray-600 mb-1">เงินเป้าหมายรวมที่อยากได้ (บาท)</label>
                    <input type="number" step="0.01" id="savings-target-x" value="1000" oninput="calculateSavingsPreview()" class="w-full px-3 py-2 border border-pink-200 rounded-xl focus:outline-none focus:border-pink-400 text-sm bg-pastel-soft">
                </div>

                <div id="savings-input-mode-days" class="hidden space-y-3">
                    <div>
                        <label class="block text-xs font-medium text-gray-600 mb-1">จำนวนวันที่ต้องการออม (วัน)</label>
                        <input type="number" id="savings-days-y" value="30" min="1" oninput="calculateSavingsPreview()" class="w-full px-3 py-2 border border-pink-200 rounded-xl focus:outline-none focus:border-pink-400 text-sm bg-pastel-soft">
                    </div>
                    <div>
                        <label class="block text-xs font-medium text-gray-600 mb-1">เงินออมต่อคนต่อครั้ง (บาท)</label>
                        <input type="number" step="0.01" id="savings-per-time-z" value="50" min="1" oninput="calculateSavingsPreview()" class="w-full px-3 py-2 border border-pink-200 rounded-xl focus:outline-none focus:border-pink-400 text-sm bg-pastel-soft">
                    </div>
                </div>

                <!-- Preview Calculation Box -->
                <div class="bg-pink-100/50 p-3 rounded-xl text-xs space-y-1 text-gray-700">
                    <div class="font-semibold text-pastel-heading">✨ ผลลัพธ์การคำนวณพรีวิว:</div>
                    <div>• เงินออมคนละ / ครั้ง: <span id="preview-z" class="font-bold text-pink-600">500.00</span> บาท</div>
                    <div>• เป้าหมายรวมทั้งกระปุก: <span id="preview-x" class="font-bold text-pink-600">1,000.00</span> บาท</div>
                    <div>• ระยะเวลาจนครบเป้า: <span id="preview-days" class="font-bold text-pink-600">2</span> วัน</div>
                </div>

                <button type="submit" class="w-full btn-pastel py-2.5 rounded-xl text-sm font-semibold flex items-center justify-center gap-2">
                    🎉 บันทึกกระปุกออมเงิน
                </button>
            </form>
        </div>
    </div>

    <script>
        // State Storage Keys
        const STORAGE_KEY = 'STORE_SAVINGS_APP_DATA_V1';

        // Initial State Data
        const defaultState = {
            activeSystem: 'savings', // 'savings', 'grocery', 'luxury'
            activeStoreSubTab: 'record', // 'record', 'analytics'
            savings: {
                "กระปุกตั้งต้น ✨": {
                    n: 2,
                    names: "ม่อน, เนเน่",
                    w: 1,
                    z: 50.0,
                    x: 1000.0
                }
            },
            grocery_sales: [
                { id: 1, date: "2026-10-05", time: 10, category: "เครื่องดื่ม", product_name: "นมสดพาสเทล", cost: 15.0, price: 25.0 },
                { id: 2, date: "2026-10-05", time: 14, category: "ขนม", product_name: "คุกกี้สตอเบอร์รี่", cost: 20.0, price: 35.0 },
                { id: 3, date: "2026-10-05", time: 14, category: "เครื่องดื่ม", product_name: "นมสดพาสเทล", cost: 15.0, price: 25.0 }
            ],
            luxury_sales: [
                { id: 1, date: "2026-10-05", time: 13, category: "กระเป๋า", product_name: "กระเป๋าถือสีชมพู", cost: 1200.0, price: 2500.0 },
                { id: 2, date: "2026-10-05", time: 16, category: "น้ำหอม", product_name: "น้ำหอมกลิ่นดอกไม้", cost: 800.0, price: 1800.0 },
                { id: 3, date: "2
