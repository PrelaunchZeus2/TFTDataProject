export class FileHandler {
    private filePath: string;

    constructor(filePath: string) {
        this.filePath = filePath;
    }

    public saveDataToCSV(data: any[]): void {
        const csvContent = this.convertToCSV(data);
        this.writeToFile(csvContent);
    }

    private convertToCSV(data: any[]): string {
        const header = Object.keys(data[0]).join(",") + "\n";
        const rows = data.map(item => Object.values(item).join(",")).join("\n");
        return header + rows;
    }

    private writeToFile(content: string): void {
        const blob = new Blob([content], { type: 'text/csv;charset=utf-8;' });
        const link = document.createElement("a");
        const url = URL.createObjectURL(blob);
        link.setAttribute("href", url);
        link.setAttribute("download", this.filePath);
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
}