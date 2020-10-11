<template>
<div class="d-flex align-item-center justify-content-center">
    <div class="card" style="width: 25rem; margin-top: 100px;">
        <div class="card-body">
            <form @submit.prevent="sendPhrase">
                <div class="form-group">
                    <label for="exampleInputEmail1">Frase</label>
                    <input type="text" class="form-control" v-model="phrase" aria-describedby="preverSentimento" placeholder="Coloque a frase aqui">
                    <small class="form-text text-muted">A frase digitada terá o sentimento classificado como felicidade, tristeza ou raiva.</small>
                </div>
                <div class="form-check">
                    <input type="checkbox" class="form-check-input" v-model="statistic" :disabled="!predict">
                    <label class="form-check-label" for="exampleCheck1">Mostrar estatísticas</label>
                </div>
                <button type="submit" class="btn btn-success">Prever</button>
            </form>
        </div>
        <div class="card" style="width: 25rem;">
            <div class="card-body">
                <div v-if="predict">
                    <strong class="card-text">Sentimento previsto: </strong>
                    <span class="card-text">{{(response.predicao)}}</span>
                </div>
                <div v-if="!predict">
                    <span>A predição aparecerá aqui</span>
                </div>
                <div v-if="statistic">
                    <div v-for="(prob, index) in response.probabilidades" :key="index">
                        <p class="card-text">{{index}}: {{prob}}%</p>
                    </div>
                </div>
                <button class="btn btn-primary" :disabled="!predict" @click.prevent="restartPrediction">Reiniciar</button>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Predict',
    data: function() {
        return {
            phrase: null,
            response: null,
            predict: false,
            statistic: null
        }
    },
    methods: {
       sendPhrase() {
           this.predict = true;
           const payload = {'phrase': this.phrase}
           console.log(payload)

           const path = 'http://127.0.0.1:5000/'
           axios.post(path, payload)
            .then((res) => {
                this.response = res.data
                console.log(this.response)
            })
       },
       restartPrediction() {
           this.predict = false;
           this.phrase = null;
           this.statistic = false;
       }
    }
}
</script>