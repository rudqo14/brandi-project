<template>
  <div>
    <article class="optionInfo">
      <div class="title">
        <i class="fas fa-pencil-alt"></i>
        <span class="menuName">옵션 정보</span>
      </div>
      <div class="optionTabla">
        <template>
          <v-simple-table>
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-left">옵션 설정</th>
                  <th class="text-left">Calories</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in desserts" :key="item.name">
                  <td>{{ item.name }}</td>
                  <td>{{ item.calories }}</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </template>
      </div>
    </article>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.optionInfo {
  margin-top: 30px;
  border: 1px solid lightgray;
  border-radius: 5px;

  .title {
    display: flex;
    align-items: center;
    background-color: lightgray;
    height: 38px;
    font-size: 18px;
    padding-left: 15px;

    .menuName {
      margin-left: 10px;
    }
  }
}
</style>
