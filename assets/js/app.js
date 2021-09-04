var app2 = new Vue({
    el: '#vue-app',
    delimiters: ['${', '}'],
    data: {
        orders: [],
        businessOpen: '',
        loading: false,
        currentOrder: {},
        orderTime: new Date().toLocaleString().slice(11),
        orderID: '',
        orderReady: '',
        queue: '',
        notDoneOrders: []
    },
    created: async function() {
        await this.getOrders()
        this.getBusinessStatus()
        this.getOrderId()
        this.getQueue()
    },
    methods: {
        getCookie: function(name) {
            var value = '; ' + document.cookie
            var parts = value.split('; ' + name + '=')
            if (parts.length === 2) return parts.pop().split(';').shift()
        },
        getOrders: async function() {
            this.loading = true
            let response = await fetch('/food/orderlist/')
            let data = await response.json()
            this.orders = data
            this.loading = false
        },
        getOrder: function(id) {
            this.loading = true
            this.$http.get(`/food/orderdetail/${id}/`)
                .then((response) => {
                    this.currentOrder = response.data
                    $('#editOrderModal').modal('show')
                    this.loading = false
                })
                .catch((err) => {
                    this.loading = false
                    console.log(err)
                })
        },
        deleteOrder: function(id) {
            this.loading = true
            this.$http.delete(`/food/orderdetail/${id}/`, { headers: { 'X-CSRFToken': this.getCookie('csrftoken') } })
                .then((response) => {
                    this.loading = false
                    this.getOrders()
                })
                .catch((err) => {
                    this.loading = false
                    console.log(err)
                })
        },
        updateOrder: function() {
            this.loading = true
            this.$http.put(`/food/orderdetail/${this.currentOrder.id}/`, this.currentOrder, { headers: { 'X-CSRFToken': this.getCookie('csrftoken') } })
                .then((response) => {
                    this.loading = false
                    this.currentOrder = response.data
                    this.getOrders()
                })
                .catch((err) => {
                    this.loading = false
                    console.log(err)
                })
        },
        getBusinessStatus: function() {
            this.$http.get('/food/business/')
                .then((response) => {
                    this.businessOpen = ($(response.data).find('#business_status').text() === 'open')
                })
                .catch((err) => {
                    console.log(err)
                })
        },
        getOrderId: function() {
            if ($('.order-success > ul > li:first-child').length !== 0) {
                this.orderID = parseInt($('.order-success > ul > li:first-child').text().slice(10))
            }
        },
        doneOrder: async function(id) {
            this.loading = true
            let response = await this.$http.get(`/food/orderdetail/${id}/`)
            this.currentOrder = response.data

            this.currentOrder.done = true
            response = await this.$http.put(`/food/orderdetail/${this.currentOrder.id}/`, this.currentOrder, { headers: { 'X-CSRFToken': this.getCookie('csrftoken') } })
            this.loading = false
            this.currentOrder = response.data
            this.getOrders()
        },
        getQueue: function() {
            this.notDoneOrders = this.orders.filter(order => order.done === false)
            if (this.orderID === '') this.queue = this.notDoneOrders.length
            else this.queue = this.notDoneOrders.filter(order => order.id <= this.orderID).length
        }
    }
})

setInterval(function() {

    app2.getOrders()

    let orderStatus = app2.orders.filter(order => order['id'] === app2.orderID)[0]
    if (orderStatus != null) {
        app2.orderReady = orderStatus.done
    }


    app2.getBusinessStatus()


    app2.getQueue()
}, 7000)