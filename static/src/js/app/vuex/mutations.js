import {
  FETCH_TOKENS,
  SELECT_TOKEN,
  FETCH_NODE,
  UPDATE_TOKEN,
  SET_TEXT_ID,
  FETCH_VOCAB_LISTS,
  SET_VOCAB_LIST,
  TOGGLE_SHOW_IN_VOCAB_LIST,
  FETCH_TEXT,
  FETCH_PERSONAL_VOCAB_LIST,
  FETCH_ME,
} from '../constants';

export default {
  [FETCH_ME]: (state, data) => {
    state.me = data;
  },
  [FETCH_TEXT]: (state, data) => {
    state.text = data;
  },
  [FETCH_VOCAB_LISTS]: (state, data) => {
    state.vocabLists = data;
  },
  [FETCH_PERSONAL_VOCAB_LIST]: (state, data) => {
    state.personalVocabList = data;
  },
  [SET_TEXT_ID]: (state, id) => {
    state.textId = id;
  },
  [FETCH_TOKENS]: (state, data) => {
    state.tokens = data;
  },
  [SELECT_TOKEN]: (state, { token, data }) => {
    state.selectedToken = token;
    state.selectedTokenHistory = data.data.tokenHistory;
  },
  [FETCH_NODE]: (state, data) => {
    state.nodes = {
      ...state.nodes,
      [data.pk]: data,
    };
  },
  [UPDATE_TOKEN]: (state, data) => {
    state.tokens = data.tokens;
    state.selectedTokenHistory = data.tokenHistory;
    if (state.selectedToken) {
      state.selectedToken = state.tokens[state.selectedToken.tokenIndex];
    }
  },
  [SET_VOCAB_LIST]: (state, id) => {
    state.selectedVocabList = id;
  },
  [TOGGLE_SHOW_IN_VOCAB_LIST]: (state) => {
    state.showInVocabList = !state.showInVocabList;
  },
};
