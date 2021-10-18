<template>
  <q-page class="flex flex-center">
    <q-stepper
      v-if="step < 6"
      v-model="step"
      ref="stepper"
      color="primary"
      animated
    >
      <q-step
        v-for="(question, index) in evaluation_data['questions']"
        :key="index"
        :name="index + 1"
        :title="'Question ' + (index + 1)"
        icon="check_circle"
        :done="step > index + 1"
      >
        <div class="col">
              <div class="text-h6">Pregunta</div>
              <div class="text-h5" style="display: inline-block;">
                {{ question["question"] }}?
              </div>

          <q-option-group
            v-model="answers[index]"
            :options="question['options']"
            color="primary"
          />
        </div>
      </q-step>

      <template v-slot:navigation>
        <q-stepper-navigation>
          <q-btn
            @click="step !== 5 ? $refs.stepper.next() : this.end_evaluation()"
            color="primary"
            :label="step === 5 ? 'Terminar' : 'Siguiente'"
          />
          <q-btn
            v-if="step > 1"
            flat
            color="primary"
            @click="$refs.stepper.previous()"
            label="Back"
            class="q-ml-sm"
          />
        </q-stepper-navigation>
      </template>
    </q-stepper>

    <div v-else class="q-my-lg" style="width: 60%">
      <q-card class="my-card q-my-lg">
        <q-card-section>
          <div class="text-h4">{{ evaluation_data["name"] }}</div>
          <div class="text-subtitle1 text-positive">Correctas: {{ correct }}</div>
          <div class="text-subtitle1 text-negative">Incorrectas: {{ incorrect }}</div>
        </q-card-section>

        <q-separator inset />

        <q-card-section>
          <div
            v-for="(question, index) in evaluation_data['questions']"
            :key="index"
            class="q-my-md"
          >
            <div class="col">
              <div class="text-h6">Pregunta</div>
              <div class="text-h5" style="display: inline-block;">
                {{ question["question"] }}?
              </div>

              <q-option-group
                v-model="answers[index]"
                :options="question['options']"
                :color="
                  answers[index] == question['answer'] ? 'positive' : 'negative'
                "
                disable
              />
            </div>
          </div>
        </q-card-section>
      </q-card>

      <div class="row justify-center"> <q-btn color="primary" label="Volver" to="/"/> </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import { api } from "boot/axios";

export default defineComponent({
  name: "Evaluation",
  props: ["id"],
  data() {
    return {
      evaluation_data: {},
      step: ref(1),
      answers: [],
      correct: 0,
      incorrect: 0,
    };
  },
  methods: {
    get_data() {
      api.get("evaluations/get/" + this.id).then((res) => {
        this.evaluation_data = res.data;
      });
    },
    end_evaluation() {
      this.step = ref(6);
      let questions = this.evaluation_data["questions"];
      for(let i = 0; i < questions.length; i++){
        if(questions[i]["answer"] == this.answers[i]){
          this.correct += 1;
        } else {
          this.incorrect += 1;
        }
      }
    },
  },
  beforeMount() {
    this.get_data();
  },
});
</script>
