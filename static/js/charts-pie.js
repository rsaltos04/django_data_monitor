/**
 * For usage, visit Chart.js docs https://www.chartjs.org/docs/latest/
 */
const total_puentes = JSON.parse(document.getElementById('total_puentes').textContent);
const total_coronas = JSON.parse(document.getElementById('total_coronas').textContent);
const total_protesis = JSON.parse(document.getElementById('total_protesis').textContent);
const pieConfig = {
  type: 'doughnut',
  data: {
    datasets: [
      {
        data: [total_puentes, total_coronas, total_protesis],
        /**
         * These colors come from Tailwind CSS palette
         * https://tailwindcss.com/docs/customizing-colors/#default-color-palette
         */
        backgroundColor: ['#0694a2', '#1c64f2', '#7e3af2'],
        label: 'Dataset 1',
      },
    ],
    labels: ['Puentes', 'Coronas', 'Prótesis'],
  },
  options: {
    responsive: true,
    cutoutPercentage: 80,
    /**
     * Default legends are ugly and impossible to style.
     * See examples in charts.html to add your own legends
     *  */
    legend: {
      display: false,
    },
  },
}

// change this to the id of your chart element in HMTL
const pieCtx = document.getElementById('pie')
window.myPie = new Chart(pieCtx, pieConfig)
