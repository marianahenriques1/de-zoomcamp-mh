variable "credentials" {
    description = "My credentials"
    default = "./keys/my_creds.json"
}

variable "project" {
    description = "Project"
    default = "sound-concept-449022-t3"
}

variable "region" {
    description = "The region of the resources"
    default = "europe-west1"
}

variable "location" {
    description = "The location of the resources"
    default = "EU"
}

variable "bq_dataset_name" {
    description = "My BigQuery dataset name"
    default = "demo_dataset"
}

variable "gcs_bucket_name" {
    description = "My Storage bucket name"
    default = "sound-concept-449022-t3-terra-bucket"
}

variable "gcs_storage_class" {
    description = "Bucket Storage class"
    default = "STANDARD"
  
}