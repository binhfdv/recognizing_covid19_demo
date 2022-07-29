import { createApp } from 'vue'
import App from './App.vue'
import VueRecordAudio from './components/VueRecordAudio'

const app = createApp(App)
app.use(VueRecordAudio).mount("#app")

