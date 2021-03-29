import { createStore, combineReducers, applyMiddleware } from 'redux'
import thunk from 'redux-thunk'
import { composeWithDevTools } from 'redux-devtools-extension'
import { ProductListReducer, ProductDetailsReducer } from './reducers/ProductReducers'

const reducer = combineReducers({
    productList:ProductListReducer,
    productList:ProductDetailsReducer,
})

const initialState = {}

const middleware = [thunk]

const store = createStore(reducer, initialState,
    composeWithDevTools(applyMiddleware(...middleware)))


export default store