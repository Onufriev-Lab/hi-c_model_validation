# Your data
# Set the CRAN mirror
options(repos = c(CRAN = "https://cloud.r-project.org"))

# Dist_merge_2cubes_4Y_X <- c(1.780330085889911, 1.836516303737808, 1.8365163037378083, ... )
#install.packages(c("ggplot2","patchwork"))


# Generate random data for demonstration
#set.seed(42)
library(ggplot2)
library(patchwork)

data <- rep(c(1.780330085889911, 1.836516303737808, 1.8365163037378083, 1.853553390593274, 1.8927025215857052, 1.8927025215857054, 1.9085777065554923, 1.9085777065554925, 1.9097396084411713, 1.9244528915252794, 1.92561479))

data <- lapply(data,"*", 0.5)
data <- as.numeric(data)

standard_deviation <- sd(data)

# Create a data frame
# Create a data frame
#data1 <- data.frame(values = Dist_merge_2cubes_4Y_X)



# Plot histogram with normal distribution line
plot1 <- ggplot(data.frame(values = data), aes(x = values)) +
  geom_histogram(aes(y = ..density..), bins = 21, fill = "lightblue", color = "black") +
  geom_density(color = "red", bw = 0.04) +  # Adjust the bandwidth value (e.g., 0.1)
  labs(x= expression(paste("Mean point-to-point distance of TADs (", mu, "m)"))
       , y = "Density of valid paths with length = 100 kb") +
 
  theme_minimal()+
  theme(panel.background = element_rect(fill = "gray90"),
axis.text = element_text(size = 14, color = "black"),  # Change font of x-ticks and y-ticks
axis.title.x = element_text(size = 14, color = "black", margin = margin(t = 10)),  # Change font of x-label
axis.title.y = element_text(size = 14, color = "black", margin = margin(r = 10)))  # Change font of y-label


# Sample data
#data2<-rep(c(1.780330085889911, 1.836516303737808, 1.8365163037378083, 1.853553390593274, 1.8927025215857052, 1.8927025215857054, 1.9085777065554923, 1.9085777065554925, 1.9097396084411713, 1.9244528915252794, 1.9256147934109582, 1.925614$
#data2<-lapply(data2,"*",0.5)
#data<- as.numeric(data)

#data <- c(-1.28, 0.36, 0.77, -0.45, 1.62, -0.85, 0.91, 0.12, 0.25, -0.68)

# Step 2: Compute sample mean and sample standard deviation
sample_mean <- mean(data)
sample_std <- sd(data)

# Step 3: Use sample mean and sample standard deviation as estimates
mu_estimate <- sample_mean
sigma_estimate <- sample_std

# Step 4: Generate samples from estimated Gaussian distribution using inverse sampling
num_samples <- 93696
set.seed(10000)  # Set seed for reproducibility
samples <- mu_estimate + sigma_estimate * sqrt(2) * qnorm(runif(num_samples))

# Step 5: Repeat the sampling process multiple times and calculate mean and standard deviation
num_iterations <- 100
mean_estimates <- c()
std_estimates <- c()

for (i in 1:num_iterations) {
  samples <- mu_estimate + sigma_estimate * sqrt(2) * qnorm(runif(num_samples))
  mean_estimates <- c(mean_estimates, mean(samples))
  std_estimates <- c(std_estimates, sd(samples))
}

# Step 6: Calculate the average estimates
mean_estimate_avg <- mean(mean_estimates)
std_estimate_avg <- mean(std_estimates)

# Create the histogram with better bin width
plot2 <- ggplot(data.frame(values = samples), aes(x = values)) +
  geom_histogram(aes(y = ..density..), bins = 21, fill = "lightblue", color = "black") +
  geom_density(color = "red", bw = 0.04) +  # Adjust the bandwidth value (e.g., 0.1)
  labs(x= expression(paste("Mean point-to-point distance of TADs (", mu, "m)"))
       , y = "Density of valid paths with length = 100 kb") +
  ggtitle("") +
  theme_minimal()+
  theme(panel.background = element_rect(fill = "gray90"),
axis.text = element_text(size = 14, color = "black"),  # Change font of x-ticks and y-ticks
axis.title.x = element_text(size = 14, color = "black", margin = margin(t = 10)),  # Change font of x-label
axis.title.y = element_text(size = 14, color = "black", margin = margin(r = 10)))  # Change font of y-label
# Overlay the two plots
combined_plot <- plot1 + plot2 + plot_layout(ncol = 1)

# Save the combined plot as a PNG file
ggsave("combined_histogram_plot.png", combined_plot, width = 6, height = 4, dpi = 300)
