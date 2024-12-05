<template>
    <div class="dashboard">
        <div class="display">
            <LineChart></LineChart>
        </div>
    </div>
    
</template>

<script>
import LineChart from "./LineChart.vue"

export default{
    components:{
        LineChart,
    },
    data(){
        return{
            chartData: null,
            chartOptions: {
                responsive: true,
                plugins: {
                    title: {
                        display: true,
                        text: ""                                        //Here?
                    }
                }
            }
        }
    },
    mounted(){
        this.fetchChartData();
    },
    methods: {
        async fetchChartData() {
            try {
                const res = await axios.get("http://localhost:<port>/db/weather");                          //will be broken until db is hosted

                this.chartData = {
                    labels: res.data.labels,
                    // data: 
                }
            }catch (error){
                axios.post("http://localhost:<port>/db/err_log");
            }   
        } 
    },
}

</script>