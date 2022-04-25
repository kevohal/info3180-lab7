<template>
    <div class="container">
        <form @submit.prevent="uploadPhoto" enctype="multipart/form-data" id="uploadForm" class="form-control">
            <div class="formfield">
                <h2>Upload Form</h2>
            </div>
            <div class="formfield">
                <label for="description" >Description</label>
                <textarea name = "description" id="photo" class="form-control">Enter the description of your photo here...</textarea>   
            </div>
            
            <div class="formfield">
                <label for="photo">Photo Upload</label>
                <input type = "file" name = "photo" class="form-control">    
            </div>
            
            
            <br>
            <br>

            <div class="butn">
                <button type = "submit" class="btn btn-primary" >Submit</button>
            </div>
       
       </form>
    </div>    
</template>

<script>
    export default {
        data() {
            return{
                csrf_token: ''
            }
            
        },

        created() {
            this.getCsrfToken();

        },

        methods: {

            uploadPhoto() {

                let uploadForm = document.getElementById('uploadForm');
                let form_data = new FormData(uploadForm);

                fetch("/api/upload", {
                    method: 'POST', 
                    body: form_data,
                    headers: {
                        'X-CSRFToken': this.csrf_token
                    }
                    
                })

                    .then(function(response) {
                        return response.json();
                    })

                    .then(function (data) {
                        //display a success message
                        console.log(data);
                    })

                    .catch(function (error) {
                        console.log(error);
                    });
            },
            getCsrfToken() {
                let self = this;
                fetch('/api/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    self.csrf_token = data.csrf_token;
                })

            }
        }

    }
</script>

<style scoped>
    .formfield {
        margin: 20px;

    }

    .butn {
        margin-left: 20px;
    }
</style>
 