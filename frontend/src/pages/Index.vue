<template>
  <q-page class="flex flex-center">
    <div v-for="data_key in Object.keys(data)" :key="data_key">
      <q-card class="my-card bg-primary text-white" style="width: 300px">
        <q-card-section>
          <div class="text-h6">{{ data[data_key]["name"] }}</div>
          <div class="text-subtitle2">
            # Preguntas: {{ data[data_key]["qty"] }}
          </div>
        </q-card-section>

        <q-separator dark />
        <q-card-actions>
          <q-btn color="white" class="bg-dark" flat :to="{ name: 'evaluation', params: { id: data_key }}">Empezar</q-btn>
        </q-card-actions>
      </q-card>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import { api } from "boot/axios";

export default defineComponent({
  name: "PageIndex",
  data() {
    return {
      data: {},
    };
  },
  methods: {
    get_data() {
      api.get("evaluations/get_all").then((res) => {
        this.data = res.data;
      });
    },
  },
  beforeMount() {
    this.get_data();
  },
});
</script>
