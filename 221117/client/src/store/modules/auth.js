const HOST = `http://127.0.0.1:8000`

const axios = require('axios');
import router from '../../router';


const state = {
    token: null,
    username: null,
    errors: [],
    loading: false,
};

const getters = {
    isLoggedIn: state => !!state.token,
    getErrors: state => state.errors,
    isLoading: state => state.loading,
};

const mutations = {
    setLoading: (state, flag) => state.loading = flag,
    setToken: (state, token) => {
        state.token = token;
        // sessionStorage.setItem('jwt', token);
    },
    setUsername: (state, name) => {
        state.username = name;
        sessionStorage.setItem('username', name)
    },
    pushError: (state, error) => state.errors.push(error),
    clearErrors: state => state.errors = [],
};

const actions = {
    initialLogin: ({ commit }) => {
        const token = sessionStorage.getItem('jwt')
        if (token) {
            commit('setToken', token)
        }
    },
    logout: ( { commit }) => {
        commit('setToken', null);
        sessionStorage.removeItem('my_movies');
        sessionStorage.removeItem('my_reviews');
        sessionStorage.removeItem('username');
        router.push('/login');
    },

    pushError({ commit }, error) {
        commit('pushError', error)
    },

    login: ({ commit, getters }, credentials) => {
        commit('clearErrors')
        if (getters.isLoggedIn) {
            router.push('/');
        }
        else {
                axios.post(HOST + '/api-token-auth/', credentials)
                    .then(token => {
                        commit('setToken', token.data.token);
                        commit('setUsername', credentials.username);
                        commit('setLoading', false);
                        router.push('/');
                    })
                    .catch(err => {
                        if (!err.response) {
                            commit('pushError', 'Network Error..')
                        } else if (err.response.status === 400) {
                            commit('pushError', 'Invalid username or password');
                        } else if (err.response.status === 500) {
                            commit('pushError', 'Internal Server error. Please try again later')
                        } else {
                            commit('pushError', 'Some error occured');
                        }
                        commit('setLoading', false);
                    })
            }
    },

    validation: ({ commit, dispatch }, credentials) => {
        commit('setLoading', false);
        if (!credentials.username) {
            commit('pushError', 'username can not be empty');
            commit('setLoading', false);
        }
        if (credentials.password < 8) {
            commit('pushError', 'password too short');
            commit('setLoading', false);
        }
        else {
            dispatch('login', credentials);
        }
    },
    signup: ({ commit, getters, dispatch }, { username, nickname, password, passwordConfirmation }) => {
        commit('clearErrors')
        if (getters.isLoggedIn) {
            router.push('/');
        } else {
            commit('clearErrors');
            if (!username) {
                commit('pushError', '유저네임을 입력하세요');
            } if (!nickname) {
                commit('pushError', '닉네임을 입력하세요');
            } if (password.length < 8) {
                commit('pushError', '비밀번호는 8자 이상이어야 합니다');
            } else {
                if (password === passwordConfirmation) {
                    axios({
                        method: 'post',
                        url: `${HOST}/dj-rest-auth/signup/`,
                        data: {
                            username,
                            nickname,
                            password,
                        },
                    })
                    .then(response => {
                        const credentials = {
                            username,
                            nickname,
                            password,
                        }
                        console.log(response)
                        console.log('회원가입성공')
                        dispatch('login', credentials);
                        
                    })
                    .catch(err => {
                        if (!err.response) {
                            commit('pushError', 'Network Error..')
                        } else {
                            commit('pushError', 'Some error occured');
                        }
                    })
                } else {
                    commit('pushError', '비밀번호가 일치하지 않습니다');
                }
            }
        }
    }
};

export default {
    state,
    getters,
    mutations,
    actions
}