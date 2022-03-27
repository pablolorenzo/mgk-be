<template>
  <div class="column items-start" style="height: 150px; background-color:red;">
    <div class="col">
      HEADER BARRR
    </div>
    <q-scroll-area class="col" style="height:100%;" >
          <q-list>
            <q-item
              v-for="(service, index) in services"
              :key="service.id"
              clickable
              v-ripple
            >
              <q-item-section avatar>
                <q-avatar>
                </q-avatar>
              </q-item-section>

              <q-item-section>
                <q-item-label lines="1">
                  {{ service.address }}
                </q-item-label>
                <q-item-label class="conversation__summary" caption>
                  
                  {{ service.status_id }}
                </q-item-label>
              </q-item-section>

              <q-item-section side>
                <q-item-label caption>
                  {{ service.provider_id }}
                </q-item-label>
                <q-icon name="keyboard_arrow_down" />
              </q-item-section>
            </q-item>
          </q-list>
        </q-scroll-area>
</div>
</template>

<script>


import { mapActions, mapState } from 'vuex';

export default {
  name: 'Services',
  components: {
  },
  computed: {
    ...mapState({
      services: (state) => state.services.services,
    }),
  },
  methods: {
    ...mapActions({
      getServices: 'services/getServices',
    }),
  },
  mounted() {
    this.getServices()
    console.log("##############################");
    console.log(this)
  },

}
</script>
