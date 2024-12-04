<template>
    <div>
        <canvas ref="chartCanvas"></canvas>
    </div>
</template>

<script>
import {Chart, LineController, LineElement, PointElement, LinearScale, Title, Tooltip, CategoryScale } from 'chart.js';

Chart.register(LineController, LineElement, PointElement, LinearScale, Title, Tooltip, CategoryScale);

export default {
    name: "LineChart",
    props:{
        chartData: {
            type: Object,
            required: true,
        },
        ChartOptions:{
            type: Object,
            default: () => ({}),
        },
    },
    data(){
        return{
            chartInstance: null,
        };
    },
    mounted(){
        this.createChart();
    },
    methods:{
        createChart(){
            const ctx = this.$refs.chartCanvas.getContext("2d");
            this.chartInstance = new Chart(ctx, {
            type: "line",
            data: this.chartData,
            options: this.chartOptions,
            });
        },
        updateChart() {
            if (this.chartInstance) {
                this.chartInstance.data = this.chartData;
                this.chartInstance.options = this.chartOptions;
                this.chartInstance.update();
            }
        },
        watch: {
            chartData: "updateChart",
            chartOptions: "updateChart",
        },
        beforeDestroy(){
            if(this.chartInstance){
                this.chartInstance.destroy();
            }
        }
    },

}

</script>