<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
    >
      <v-list dense v-if="isLoggedIn">
        <v-list-item link to="/">
          <v-list-item-action>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Movie List</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link to="/worldcup">
          <v-list-item-action>
            <v-icon>mdi-alpha-w-box</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>World Cup</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item link to="/profile">
          <v-list-item-action>
            <v-icon>mdi-account</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Profile</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item @click.prevent="logout">
          <v-list-item-action>
            <v-icon>mdi-alpha-l-box</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Log out</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-list dense v-else>
        <v-list-item link to="/">
          <v-list-item-action>
            <v-icon>mdi-account-check</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Log in</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link to="signup">
          <v-list-item-action>
            <v-icon>mdi-account-plus</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Sign up</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      clipped-left
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Movie Cave</v-toolbar-title>
    </v-app-bar>

    <v-content class="row">
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col>
            <router-view></router-view>
          </v-col>
        </v-row>
      </v-container>
    </v-content>

    <v-footer app>
      <span>&copy; 2019 Y2GB</span>
    </v-footer>
  </v-app>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex';
  export default {
    name: 'App',
    methods: {
      ...mapActions(['login', 'logout']),
    },
    computed: {
      ...mapGetters(['isLoggedIn']),
    },
    props: {
      source: String,
    },
    data: () => ({
      drawer: null,
    }),
    created () {
      this.$store.dispatch('initialLogin')
      this.$vuetify.theme.dark = true
    },
  }
</script>