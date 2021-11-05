#include <gtest/gtest.h>
#include <library.h>

TEST(TestBlock, Addition) { 
    using namespace company::project;
    ASSERT_EQ(6, function(2, 4));
}
 
TEST(TestBlock, Subtraction) {
    using namespace company::project;
    ASSERT_EQ(-2, function(2, -4));
}
 
int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
