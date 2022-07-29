<template>
<div class="background" :class="{ otherColor: isSignIn }">

  <div class="page-loader" v-if="!isLoaded">
    <div style="background-color: #8cc271" class="cube first"></div>
    <div style="background-color: #69beeb" class="cube"></div>
    <div style="background-color: #f5aa39" class="cube"></div>
    <div style="background-color: #e9643b" class="cube last"></div>
  </div>

  <div id="head">
      <p content="width=device-width, initial-scale=1">ĐỀ TÀI: NHẬN DIỆN TIẾNG HO COVID-19
      <a target="_blank" style="color: #01256b;" href="https://github.com/githubbinh/recognizing_covid19_demo"><img src="./assets/logo.png" alt="img" border="0" style="width: 32px"/></a>
      </p>
  </div>

  <div>
        <div id="up">
          <button id="button" onclick="document.getElementById('inputfile').click()">CHỌN FILE</button>
          <input type='file' id="inputfile" style="display:none" @change="onFileChange">
          <button id="button" v-on:click="isHidden = !isHidden">Metadata</button>
        </div>

        <table v-if="!isHidden" id="table" style="max-height: 75x; overflow-y: scroll">
          <tr>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          </tr>
          <tr>
            <td>Tuổi:<br><input type="text" name=" age " v-model=" age " style="background-color:#d6eaf2"><br>
                Giới Tính:<br><input type="text" name=" gender " v-model=" gender " style="background-color:#d6eaf2"><br>
                Quốc Gia:<br><input type="text" name=" country " v-model=" country " style="background-color:#d6eaf2"><br>
                Khu vực:<br><input type="text" name=" locality " v-model=" locality " style="background-color:#d6eaf2"><br>
                Tỉnh/thành:<br><input type="text" name=" state " v-model=" state " style="background-color:#d6eaf2"><br>
                Có thực hiện CT scan:<br><input type="text" name=" has_ctScan " v-model=" has_ctScan " style="background-color:#d6eaf2"><br>
                Ngày làm CT scan:<br><input type="text" name=" date_of_ct_scan " v-model=" date_of_ct_scan " style="background-color:#d6eaf2"><br>
                Điểm CT scan:<br><input type="text" name=" ct_score " v-model=" ct_score " style="background-color:#d6eaf2"><br>
            </td>
            <td>Loại test COVID-19:<br><input type="text" name=" test_type " v-model=" test_type " style="background-color:#d6eaf2"><br>
                Kết quả test COVID-19:<br><input type="text" name=" test_status " v-model=" test_status " style="background-color:#d6eaf2"><br>
                Đã tiêm Vác-xin:<br><input type="text" name=" vaccination_status " v-model=" vaccination_status " style="background-color:#d6eaf2"><br>
                Tình trạng hệ hô hấp:<br><input type="text" name=" respiratory_condition " v-model=" respiratory_condition " style="background-color:#d6eaf2"><br>
                Tiền án bệnh hệ hô hấp?:<br><input type="text" name=" is_others_preexist_conditions " v-model=" is_others_preexist_conditions " style="background-color:#d6eaf2"><br>
                Có hút thuốc?:<br><input type="text" name=" is_smoker " v-model=" is_smoker " style="background-color:#d6eaf2"><br>
                Có dùng khẩu trang?:<br><input type="text" name=" is_using_mask " v-model=" is_using_mask " style="background-color:#d6eaf2"><br>
                Đau mỏi cơ và sốt:<br><input type="text" name=" fever_muscle_pain " v-model=" fever_muscle_pain " style="background-color:#d6eaf2"><br>
            </td>
            <td>Ho?:<br><input type="text" name=" is_cough " v-model=" is_cough " style="background-color:#d6eaf2"><br>
                Sốt?:<br><input type="text" name=" is_fever " v-model=" is_fever " style="background-color:#d6eaf2"><br>
                Mất mùi vị?:<br><input type="text" name=" is_loss_of_smell " v-model=" is_loss_of_smell " style="background-color:#d6eaf2"><br>
                Đau cơ?:<br><input type="text" name=" is_muscle_pain " v-model=" is_muscle_pain " style="background-color:#d6eaf2"><br>
                Khó thở?:<br><input type="text" name=" is_breathing_difficulty " v-model=" is_breathing_difficulty " style="background-color:#d6eaf2"><br>
                Mệt mỏi?:<br><input type="text" name=" is_fatigue " v-model=" is_fatigue " style="background-color:#d6eaf2"><br>
                Đau cổ họng?:<br><input type="text" name=" is_sore_throat " v-model=" is_sore_throat " style="background-color:#d6eaf2"><br>
                Cảm lạnh:<br><input type="text" name=" is_cold " v-model=" is_cold " style="background-color:#d6eaf2"><br>
            </td>
            <td>Bệnh mãn tính liên quan phổi?:<br><input type="text" name=" is_chronic_lung_disease " v-model=" is_chronic_lung_disease " style="background-color:#d6eaf2"><br>
                Bệnh liên quan tới tim?:<br><input type="text" name=" is_ischemic_heart_disease " v-model=" is_ischemic_heart_disease " style="background-color:#d6eaf2"><br>
                Bệnh liên quan tới huyết áp:<br><input type="text" name=" is_hypertension " v-model=" is_hypertension " style="background-color:#d6eaf2"><br>
                Tiêu chảy?:<br><input type="text" name=" is_diarrheoa " v-model=" is_diarrheoa " style="background-color:#d6eaf2"><br>
                Tiểu đường?:<br><input type="text" name=" is_diabetes " v-model=" is_diabetes " style="background-color:#d6eaf2"><br>
                Hen xuyễn?:<br><input type="text" name=" is_asthma " v-model=" is_asthma " style="background-color:#d6eaf2"><br>
                Viêm phổi?:<br><input type="text" name=" is_neumonia " v-model=" is_neumonia " style="background-color:#d6eaf2"><br>
                Các triệu chứng về hô hấp khác?:<br><input type="text" name=" is_others_resp " v-model=" is_others_resp " style="background-color:#d6eaf2"><br>
            </td>
          </tr>
        </table>
  </div>

  <div id="up" class ="terms_1">
    <button id="process" @click="onProcess">DỰ ĐOÁN</button>
  </div>

    <div style="padding-left: 1%;">
                <button id="button1" v-on:click="isHidden2 = !isHidden2" ><p>Ghi âm</p>
                    <vue-record-audio :mode="recordMode.audio" @stream="onStream" @result="onResult"/>
                </button>
    </div>

  <div id="down">

      <div id="left">
        <p v-if ="!isHidden2">Đang thu...</p>
        <audio controls v-if="url" :key="url">
          <source :src="url" alt="file đầu vào" type="audio/wav">
        </audio>
      </div>
      <div id="right">
        <h2 style="color: black">
          Kết quả:
          <span v-if="res" v-bind:class="{low: low, low_mid: low_mid, mid: mid, mid_high: mid_high, high: high}">{{ res }}</span>
        </h2>
      </div>
  </div>

  <footer>
  <div class="flex w-full rounded-xl bg-white p-5 mb-auto my-5 justify-between mb-10">
      <div  class="" style="height:50px; width:356px;">
        <h5 style="font-size:15px">
            <b>Khóa luận tốt nghiệp Ngành Khoa học Dữ liệu</b>
        </h5>
            <p><b>SVTH</b>: Dương Văn Bình - Lê Trần Hoài Ân</p>
            <p><b>GVHD</b>: TS. Đỗ Trọng Hợp - ThS. Tạ Thu Thủy</p>
      </div>

      <div class="" style="float:right;">
       <img src="./assets/uit.png" alt="img" border="0" style="width: 356px"/>
      </div>
    </div>
    <div style="height: 50px;"></div>
  </footer>
</div>

</template>

<script>

function downloadBlob(blob, name = 'file.txt') {
    if (
      window.navigator &&
      window.navigator.msSaveOrOpenBlob
    ) return window.navigator.msSaveOrOpenBlob(blob);

    // For other browsers:
    // Create a link pointing to the ObjectURL containing the blob.
    const data = window.URL.createObjectURL(blob);

    const link = document.createElement('a');
    link.href = data;
    link.download = name;

    link.style.display = 'none';
    document.body.appendChild(link);

    link.click();
    document.body.removeChild(link);


    // this is necessary as link.click() does not work on the latest firefox
    //link.dispatchEvent(
    //  new MouseEvent('click', {
    //    bubbles: true,
    //    cancelable: true,
    //    view: window
    //  })
    //);

    setTimeout(() => {
      // For Firefox it is necessary to delay revoking the ObjectURL
      window.URL.revokeObjectURL(data);
      link.remove();
    }, 100);
}

import VueRecordAudio from "./components/VueRecordAudio";

export default {
  name: 'App',
  components : {VueRecordAudio},
  data() {
    return {
      recordMode: {audio: 'press',video: 'press'},
      recordings: [],
      isHidden: true,
      isHidden2: true,
      isLoaded: false,
      file: null,
      url: null,
      res: null,
      fd: null,
      low: null,
      low_mid: null,
      mid: null,
      mid_high: null,
      high: null,
        name: 'unknown',
        age: 'unknown',
        is_english_proficiency : 'unknown',
        gender : 'unknown',
        country : 'unknown',
        locality : 'unknown',
        state : 'unknown',
        is_returning_user : 'unknown',
        is_smoker : 'unknown',
        is_cold : 'unknown',
        is_hypertension : 'unknown',
        is_diabetes : 'unknown',
        is_cough : 'unknown',
        date_of_ct_scan : 'unknown',
        has_ctScan : 'unknown',
        ct_score : 'unknown',
        is_diarrheoa : 'unknown',
        is_fever : 'unknown',
        is_loss_of_smell : 'unknown',
        is_muscle_pain : 'unknown',
        test_type : 'unknown',
        test_status : 'unknown',
        is_using_mask : 'unknown',
        vaccination_status : 'unknown',
        is_breathing_difficulty : 'unknown',
        is_others_resp : 'unknown',
        is_fatigue : 'unknown',
        is_sore_throat : 'unknown',
        is_ischemic_heart_disease : 'unknown',
        is_asthma : 'unknown',
        is_others_preexist_conditions : 'unknown',
        is_chronic_lung_disease : 'unknown',
        is_neumonia : 'unknown',
        latitude : 'unknown',
        longitude : 'unknown',
        respiratory_condition : 'unknown',
        fever_muscle_pain : 'unknown',
        status : 'unknown',
        quality_1 : 'unknown',
        cough_type_1 : 'unknown',
        dyspnea_1 : 'unknown',
        wheezing_1 : 'unknown',
        stridor_1 : 'unknown',
        choking_1 : 'unknown',
        congestion_1 : 'unknown',
        nothing_1 : 'unknown',
        diagnosis_1 : 'unknown',
        severity_1 : 'unknown',
        quality_2 : 'unknown',
        cough_type_2 : 'unknown',
        dyspnea_2 : 'unknown',
        wheezing_2 : 'unknown',
        stridor_2 : 'unknown',
        choking_2 : 'unknown',
        congestion_2 : 'unknown',
        nothing_2 : 'unknown',
        diagnosis_2 : 'unknown',
        severity_2 : 'unknown',
        quality_3 : 'unknown',
        dyspnea_3 : 'unknown',
        wheezing_3 : 'unknown',
        stridor_3 : 'unknown',
        choking_3 : 'unknown',
        congestion_3 : 'unknown',
        nothing_3 : 'unknown',
        cough_type_3 : 'unknown',
        diagnosis_3 : 'unknown',
        severity_3 : 'unknown',
        num_chunk : 'unknown',
    }
  },
  mounted() {
    document.onreadystatechange = () => {
      if (document.readyState == "complete") {
        this.isLoaded = true;
      }
    }
  },
  methods: {
    removeRecord (index) {
      this.recordings.splice(index)
    },
    onStream (stream) {
      console.log('Got a stream object:', stream);
    },
    onVideoStream (stream) {
      console.log('Got a video stream object:', stream);
    },
    onVideoResult (data) {
      this.$refs.Video.srcObject = null
      this.$refs.Video.src = window.URL.createObjectURL(data)
    },
    onResult (data) {
      downloadBlob(data, 'myfile.webm');
      this.isHidden2 = true;
      this.recordings.push({
        src: window.URL.createObjectURL(data)
      })
    },
    onFileChange(e) {
      this.file = e.target.files[0];
      console.log(this.file);
      this.url = URL.createObjectURL(this.file);
    },
    onProcess() {
      this.isLoaded = false;
      this.fd = new FormData();
        this.fd.append("file",this.formData);
        this.fd.append("name",this.name);
        this.fd.append("url",this.url);
        this.fd.append("is_english_proficiency", this.is_english_proficiency);
        this.fd.append("gender", this.gender);
        this.fd.append("country", this.country);
        this.fd.append("locality", this.locality);
        this.fd.append("state", this.state);
        this.fd.append("is_returning_user", this.is_returning_user);
        this.fd.append("is_smoker", this.is_smoker);
        this.fd.append("is_cold", this.is_cold);
        this.fd.append("is_hypertension", this.is_hypertension);
        this.fd.append("is_diabetes", this.is_diabetes);
        this.fd.append("is_cough", this.is_cough);
        this.fd.append("date_of_ct_scan", this.date_of_ct_scan);
        this.fd.append("has_ctScan", this.has_ctScan);
        this.fd.append("ct_score", this.ct_score);
        this.fd.append("is_diarrheoa", this.is_diarrheoa);
        this.fd.append("is_fever", this.is_fever);
        this.fd.append("is_loss_of_smell", this.is_loss_of_smell);
        this.fd.append("is_muscle_pain", this.is_muscle_pain);
        this.fd.append("test_type", this.test_type);
        this.fd.append("test_status", this.test_status);
        this.fd.append("is_using_mask", this.is_using_mask);
        this.fd.append("vaccination_status", this.vaccination_status);
        this.fd.append("is_breathing_difficulty", this.is_breathing_difficulty);
        this.fd.append("is_others_resp", this.is_others_resp);
        this.fd.append("is_fatigue", this.is_fatigue);
        this.fd.append("is_sore_throat", this.is_sore_throat);
        this.fd.append("is_ischemic_heart_disease", this.is_ischemic_heart_disease);
        this.fd.append("is_asthma", this.is_asthma);
        this.fd.append("is_others_preexist_conditions", this.is_others_preexist_conditions);
        this.fd.append("is_chronic_lung_disease", this.is_chronic_lung_disease);
        this.fd.append("is_neumonia", this.is_neumonia);
        this.fd.append("age", this.age);
        this.fd.append("latitude", this.latitude);
        this.fd.append("longitude", this.longitude);
        this.fd.append("respiratory_condition", this.respiratory_condition);
        this.fd.append("fever_muscle_pain", this.fever_muscle_pain);
        this.fd.append("status", this.status);
        this.fd.append("quality_1", this.quality_1);
        this.fd.append("cough_type_1", this.cough_type_1);
        this.fd.append("dyspnea_1", this.dyspnea_1);
        this.fd.append("wheezing_1", this.wheezing_1);
        this.fd.append("stridor_1", this.stridor_1);
        this.fd.append("choking_1", this.choking_1);
        this.fd.append("congestion_1", this.congestion_1);
        this.fd.append("nothing_1", this.nothing_1);
        this.fd.append("diagnosis_1", this.diagnosis_1);
        this.fd.append("severity_1", this.severity_1);
        this.fd.append("quality_2", this.quality_2);
        this.fd.append("cough_type_2", this.cough_type_2);
        this.fd.append("dyspnea_2", this.dyspnea_2);
        this.fd.append("wheezing_2", this.wheezing_2);
        this.fd.append("stridor_2", this.stridor_2);
        this.fd.append("choking_2", this.choking_2);
        this.fd.append("congestion_2", this.congestion_2);
        this.fd.append("nothing_2", this.nothing_2);
        this.fd.append("diagnosis_2", this.diagnosis_2);
        this.fd.append("severity_2", this.severity_2);
        this.fd.append("quality_3", this.quality_3);
        this.fd.append("dyspnea_3", this.dyspnea_3);
        this.fd.append("wheezing_3", this.wheezing_3);
        this.fd.append("stridor_3", this.stridor_3);
        this.fd.append("choking_3", this.choking_3);
        this.fd.append("congestion_3", this.congestion_3);
        this.fd.append("nothing_3", this.nothing_3);
        this.fd.append("cough_type_3", this.cough_type_3);
        this.fd.append("diagnosis_3", this.diagnosis_3);
        this.fd.append("severity_3", this.severity_3);
        this.fd.append("num_chunk", this.num_chunk);
        this.fd.append("audio_1", this.file);
        this.fd.append("audio", this.file);
      fetch("http://localhost:8000/api/predict/", {method: "POST", body: this.fd})
      .then(response => response.json())
      .then(data => {
        this.res = data["prob"]
        if (.3 - this.res >= 1e-9) {
          this.low = true;
          this.low_mid = false
          this.mid = false;
          this.mid_high = false;
          this.high = false
        } else if (.5 - this.res > 1e-9) {
          this.low = false;
          this.low_mid = true;
          this.mid = false;
          this.mid_high = false;
          this.high = false;
        }
        else if (.7 - this.res >= 1e-9) {
          this.low = false;
          this.low_mid = false;
          this.mid = true;
          this.mid_high = false;
          this.high = false;
        } else if (.8 - this.res >= 1e-9) {
          this.low = false;
          this.low_mid = false;
          this.mid = false;
          this.mid_high = true
          this.high = false;
        } else {
          this.low = false;
          this.low_mid = false;
          this.mid = false;
          this.mid_high = false;
          this.high = true;
        }
        this.isLoaded = true;
      });
    },
  },
}

</script>

<style>

#apple {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: flex;
  justify-content: center;
}

.audio{
    width: 400px;
    height: 100px;
    border-radius: 20px;
    padding: 20px;
    border: 2px solid #757575;
    margin: 50px auto;
}

.audio audio{
    outline: none;
}

.background {
  height: 90vh;
  width: 98vw;
  background-color: #f3f0ec;
}

.otherColor {
  background-color: blue;
}

@keyframes left {
  40% {
    transform: translateX(-60px);
  }
  50% {
    transform: translateX(0);
  }
}

@keyframes right {
  40% {
    transform: translateX(60px);
  }
  50% {
    transform: translateX(0);
  }
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  padding-left: 0%;
  padding-right: 0%;
}

div {
  border-radius: 12px;
}

.page-loader {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(3, 3, 3, .3);
  z-index: 999;
}

.cube {
  width: 40px;
  height: 40px;
  margin-right: 10px;
}

.first {
  animation: left 1s infinite;
}

.last {
  animation: right 1s infinite .5s;
}

#head {
    padding: 15px;
    text-align: center;
    background-color: #d6eaf2;
    font-size: 30px;
    font-weight: bold;
    color: #01256b;
    margin: 1%;
}
#head_1 {
    padding: 15px;
    text-align: center;
    justify-content: center;
    font-size: 20px;
    font-weight: bold;
    color: black;
    margin: 1%;
    background-color: #6B7175;
}

#up {
    padding: 1px 1px;
    margin: 1%;
    padding-left: 37%;
}


#logohcmut {
    width: 50%;
    height: 50%;
    cursor: pointer;
}

#logouit {
    width: 60%;
    height: 60%;
    cursor: pointer;
}

.button:active {
    background-color: red;
}

#button {
    display: block;
    background-color: white;
    border: 2px solid #074B80;
    color: black;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 12px;
    margin-right: 10px;
}

#button1 {
    display: block;
    background-color: white;
    border: 2px solid #074B80;
    color: black;

    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 14px;
    border-radius: 75px;
    margin-right: 5px;
}

#button2 {
    display: block;
    background-color: white;
    border: 2px solid #074B80;
    color: black;
    padding: 5px 40px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 12px;
    margin-right: 10px;
}
#process {
    display: block;
    background-color: white;
    border: 2px solid #4CAF50;
    color: black;
    padding: 15px 110px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 12px;
}

#button:hover {
    background-color: #074B80;
    color: white;
    cursor: pointer;
}
#button1:hover {
    background-color: #074B80;
    color: white;
    cursor: pointer;
}

#process:hover {
    background-color: #4CAF50;
    color: white;
    cursor: pointer;
}

#left {
    float: left;
    background: #d6eaf2;
    width: 48%;
    height: 200px;
    margin: 1%;
    display: flex;
    align-items: center;
    justify-content: center;
}

#right {
    float: right;
    background: #d6eaf2;
    width: 48%;
    height: 200px;
    margin: 1%;
    display: flex;
    align-items: center;
    justify-content: center;
}

#table {
    float: left;
    width: 98%;
    height: 700px;
    display: flex;
    margin: 1%;
    align-items: left;
    justify-content: center;
    background-color: #d6eaf2;
    max-height: 110px;
    overflow-y: scroll;
}


.low {
    color: #00ff55;
    display: block;
    margin: 10px 10px;
}

.low_mid {
    color: #66f706;
    display: block;
    margin: 10px 10px;
}

.mid {
    color: #fffb00;
    display: block;
    margin: 10px 10px;
}

.mid_high {
    color: #ff7b00;
    display: block;
    margin: 10px 10px;
}

.high {
    color: #ff0000;
    display: block;
    margin: 10px 10px;
}

.vue-audio-recorder, .vue-video-recorder {
  margin-right: 16px;
}

.record-settings {
  margin-top: 16px;
  display: flex;
  justify-content: flex-end;
}

.recorded-audio {
  height: 100px;
  overflow: auto;
  border: thin solid #eee;
  background-color: #f7f7f7;
  padding: 10px 5px;
  .recorded-item {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1px;
  }
  .audio-container {
    display: flex;
    height: 54px;
    margin-right: 16px;
  }
}

.recorded-video {
  video {
    width: 100%;
    max-height: 400px;
  }
}


footer {
    margin: 1%;
    text-align: left;
    color: #074B80;
    font-size: 15px;
    margin-top: 8%;
}

</style>
