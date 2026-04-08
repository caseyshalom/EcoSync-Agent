from langchain.tools import tool

@tool
def check_waste_level(area_name: str):
    """Gunakan untuk mengecek volume sampah di area tertentu (simulasi data IoT)."""
    # Di sini bisa diintegrasikan dengan API publik atau Mock Data
    return f"Area {area_name} saat ini memiliki kapasitas sampah 85%. Rekomendasi: Segera angkut."

@tool
def calculate_carbon_impact(action_type: str):
    """Menghitung estimasi pengurangan karbon berdasarkan tindakan yang diambil."""
    if "recycle" in action_type.lower():
        return "Pengurangan emisi: 2.5kg CO2."
    return "Pengurangan emisi: 0.5kg CO2."

environmental_tools = [check_waste_level, calculate_carbon_impact]