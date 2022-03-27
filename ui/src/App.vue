<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-toolbar-title>
          MAGIC KEY
        </q-toolbar-title>
      </q-toolbar>

      <q-tabs align="left">
        <q-route-tab to="/servicios" label="SERVICIOS" />
        <q-route-tab to="/gastos" label="GASTOS" />
        <q-route-tab to="/estadisticas" label="ESTADISTICAS" />
      </q-tabs>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>


<script>
import { ref } from 'vue'
export default {
  // Cambiamos los delimiters de las variables para que sean diferentes a los de Django
   delimiters: ['${', '}'],
  compilerOptions: {
    delimiters: ["${", "}$"]
  },
  // Activamos el componente dentro de la app
  components : {
  },
  // Creamos variable msg reactiva con ref
  data () {
    return {
      msg: ref('Componente de VueJS 3')
    }
  },
  name: 'LayoutDefault',
  setup () {
    return {
      leftDrawerOpen: ref(false)
    }
  }
}
</script>
